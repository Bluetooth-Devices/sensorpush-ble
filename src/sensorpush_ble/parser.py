"""Parser for SensorPush BLE advertisements.

This file is shamelessly copied from the following repository:
https://github.com/Ernst79/bleparser/blob/c42ae922e1abed2720c7fac993777e1bd59c0c93/package/bleparser/sensorpush.py

MIT License applies.
"""

from __future__ import annotations

import logging
import struct

from bleak import BleakClient
from bleak.backends.device import BLEDevice
from bleak_retry_connector import establish_connection
from bluetooth_data_tools import short_address
from bluetooth_sensor_state_data import BluetoothData
from habluetooth import BluetoothServiceInfoBleak
from sensor_state_data import SensorLibrary, SensorUpdate
from sensor_state_data.description import BaseSensorDescription

_LOGGER = logging.getLogger(__name__)

SENSORPUSH_DEVICE_TYPES = {1: "HT1", 64: "HTP.xw", 65: "HT.w", 66: "TC.x"}

SENSORPUSH_MANUFACTURER_DATA_LEN = {
    3: "HT.w",
    5: "HTP.xw",
    2: "TC.x",
}

LOCAL_NAMES = {
    "HTP.xw": "HTP.xw",
    "HT.w": "HT.w",
    "TC": "TC.x",
    "TC.x": "TC.x",
}

SENSORPUSH_SERVICE_UUID_HT1 = "ef090000-11d6-42ba-93b8-9dd7ec090aa9"
SENSORPUSH_SERVICE_UUID_V2 = "ef090000-11d6-42ba-93b8-9dd7ec090ab0"

# Battery voltage is not advertised, it can only be read over GATT from the
# second generation service. The characteristic holds two little endian
# uint16s: the cell voltage in millivolts, and the temperature in degrees
# celsius at the time of that reading.
CHARACTERISTIC_BATTERY = "ef090007-11d6-42ba-93b8-9dd7ec090aa9"

# SensorPush documents the devices as functional down to around 2400mV. A
# fresh cell measures a little over 3000mV.
BATTERY_MIN_MV = 2400
BATTERY_MAX_MV = 3000

# The device only refreshes the battery reading when a connection is
# established, and connecting spends some of the battery we are trying to
# measure, so poll no more than once a day.
POLL_INTERVAL_SECONDS = 86400

SENSORPUSH_PACK_PARAMS = {
    64: [[-40.0, 140.0, 0.0025], [0.0, 100.0, 0.0025], [30000.0, 125000.0, 1.0]],
    65: [[-40.0, 125.0, 0.0025], [0.0, 100.0, 0.0025]],
    66: [[-200.0, 1800.0, 0.0625]],
}

SENSORPUSH_DATA_TYPES = {
    1: [SensorLibrary.TEMPERATURE__CELSIUS, SensorLibrary.HUMIDITY__PERCENTAGE],
    64: [
        SensorLibrary.TEMPERATURE__CELSIUS,
        SensorLibrary.HUMIDITY__PERCENTAGE,
        SensorLibrary.PRESSURE__MBAR,
    ],
    65: [SensorLibrary.TEMPERATURE__CELSIUS, SensorLibrary.HUMIDITY__PERCENTAGE],
    66: [SensorLibrary.TEMPERATURE__CELSIUS],
}


def _find_latest_data(
    manufacturer_data: dict[int, bytes], is_ht1: bool
) -> bytes | None:
    for id_ in reversed(list(manufacturer_data)):
        data = int(id_).to_bytes(2, byteorder="little") + manufacturer_data[id_]
        if is_ht1:
            return data

        page_id = data[0] & 0x03
        if page_id == 0:
            return data
    return None


def relative_humidity_from_raw_humidity(num: int) -> float:
    int_value = (-6.0) + (125.0 * (num / (pow(2.0, 12.0))))
    if int_value < 0.0:
        int_value = 0.0

    if int_value > 100.0:
        return 100.0
    return round(int_value, 2)


def temperature_celsius_from_raw_temperature(num: int) -> float:
    return round((-46.85) + (175.72 * (num / (pow(2.0, 14.0)))), 2)


def decode_ht1_values(mfg_data: bytes) -> dict[BaseSensorDescription, float]:
    """Decode values for HT1."""
    if len(mfg_data) < 4:
        return {}

    device_type = (mfg_data[3] & 124) >> 2
    if device_type != 1:
        _LOGGER.debug("Unsupported device type: %s", device_type)
        return {}

    relative_humidity = relative_humidity_from_raw_humidity(
        (mfg_data[0] & 255) + ((mfg_data[1] & 15) << 8)
    )
    temperature_celsius = temperature_celsius_from_raw_temperature(
        ((mfg_data[1] & 255) >> 4)
        + ((mfg_data[2] & 255) << 4)
        + ((mfg_data[3] & 3) << 12)
    )

    return {
        SensorLibrary.TEMPERATURE__CELSIUS: temperature_celsius,
        SensorLibrary.HUMIDITY__PERCENTAGE: relative_humidity,
    }


def decode_values(
    mfg_data: bytes, device_type_id: int
) -> dict[BaseSensorDescription, float]:
    """Decode values."""

    if device_type_id == 1:
        return decode_ht1_values(mfg_data)

    pack_params = SENSORPUSH_PACK_PARAMS.get(device_type_id, None)
    if pack_params is None:
        _LOGGER.error("SensorPush device type id %s unknown", device_type_id)
        return {}

    values = {}

    packed_values = 0
    for i in range(1, len(mfg_data)):
        packed_values += mfg_data[i] << (8 * (i - 1))

    mod = 1
    div = 1
    for i, block in enumerate(pack_params):
        min_value = block[0]
        max_value = block[1]
        step = block[2]
        mod *= int((max_value - min_value) / step + step / 2.0) + 1
        value_count = int((packed_values % mod) / div)
        data_type = SENSORPUSH_DATA_TYPES[device_type_id][i]
        value = round(value_count * step + min_value, 2)
        if data_type == SensorLibrary.PRESSURE__MBAR:
            value = value / 100.0
        values[data_type] = value
        div *= int((max_value - min_value) / step + step / 2.0) + 1

    return values


def battery_percentage_from_millivolts(voltage_mv: int) -> int:
    """Estimate the remaining battery percentage from the cell voltage.

    This is a linear estimate over a coin cell's non-linear discharge curve, so
    expect it to sit near full for most of the cell's life and then fall away
    quickly towards the end.
    """
    percentage = (voltage_mv - BATTERY_MIN_MV) * 100 / (BATTERY_MAX_MV - BATTERY_MIN_MV)
    return round(min(100.0, max(0.0, percentage)))


def determine_device_type(
    service_info: BluetoothServiceInfoBleak, manufacturer_data: dict[int, bytes]
) -> str | None:
    """Determine the device type based on the name and UUID"""
    local_name = service_info.name

    if local_name == "s" and SENSORPUSH_SERVICE_UUID_HT1 in service_info.service_uuids:
        return "HT1"

    device_type: str | None = None
    for match_name, model_name in LOCAL_NAMES.items():
        if match_name in local_name:
            device_type = model_name

    if not device_type and SENSORPUSH_SERVICE_UUID_V2 in service_info.service_uuids:
        first_manufacturer_data_value_len = len(next(iter(manufacturer_data.values())))
        return SENSORPUSH_MANUFACTURER_DATA_LEN.get(first_manufacturer_data_value_len)

    return device_type


class SensorPushBluetoothDeviceData(BluetoothData):
    """Date update for SensorPush Bluetooth devices."""

    def __init__(self) -> None:
        """Initialize the SensorPush data."""
        super().__init__()
        self._device_type: str | None = None

    def _start_update(self, service_info: BluetoothServiceInfoBleak) -> None:
        """Update from BLE advertisement data."""
        manufacturer_data = service_info.manufacturer_data
        if not manufacturer_data:
            return

        result = {}
        device_type = determine_device_type(service_info, manufacturer_data)
        if not device_type:
            return

        self._device_type = device_type
        is_ht1 = device_type == "HT1"

        self.set_device_type(device_type)
        self.set_device_manufacturer("SensorPush")

        name = service_info.name.removeprefix("SensorPush ")
        # The name of the HT1s seems to always be "s"
        if not name or is_ht1:
            name = f"{device_type} {short_address(service_info.address)}"
        self.set_device_name(name)

        changed_manufacturer_data = self.changed_manufacturer_data(service_info)
        if not changed_manufacturer_data or len(changed_manufacturer_data) > 1:
            # If len(changed_manufacturer_data) > 1 it means we switched
            # ble adapters so we do not know which data is the latest
            # and we need to wait for the next update.
            return

        if data := _find_latest_data(changed_manufacturer_data, is_ht1):
            device_type_id = 1 if is_ht1 else 64 + (data[0] >> 2)
            if known_device_type := SENSORPUSH_DEVICE_TYPES.get(device_type_id):
                device_type = known_device_type
            result.update(decode_values(data, device_type_id))

        for data_type, value in result.items():
            self.update_predefined_sensor(data_type, value)

    def poll_needed(
        self, service_info: BluetoothServiceInfoBleak, last_poll: float | None
    ) -> bool:
        """Return True if the device should be polled for battery data.

        This is called for every advertisement, which means the device is
        online, so it is a good moment to poll if one is due.
        """
        if self._device_type is None or self._device_type == "HT1":
            # The first generation HT1 does not expose the service that carries
            # the battery voltage.
            return False

        return not last_poll or last_poll > POLL_INTERVAL_SECONDS

    async def async_poll(self, ble_device: BLEDevice) -> SensorUpdate:
        """Poll the device to retrieve the battery data.

        The device refreshes its battery reading whenever a connection is
        established, so connect, read and disconnect again rather than holding
        the connection open.
        """
        client = await establish_connection(BleakClient, ble_device, ble_device.address)
        try:
            payload = await client.read_gatt_char(CHARACTERISTIC_BATTERY)
        finally:
            await client.disconnect()

        # The second uint16 is the temperature at the time of the reading,
        # which we ignore as the advertisement carries a better one.
        (voltage_mv,) = struct.unpack_from("<H", payload)
        self.update_predefined_sensor(
            SensorLibrary.VOLTAGE__ELECTRIC_POTENTIAL_VOLT, voltage_mv / 1000
        )
        self.update_predefined_sensor(
            SensorLibrary.BATTERY__PERCENTAGE,
            battery_percentage_from_millivolts(voltage_mv),
        )
        return self._finish_update()
