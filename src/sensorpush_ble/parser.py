"""Parser for SensorPush BLE advertisements.

This file is shamelessly copied from the following repository:
https://github.com/Ernst79/bleparser/blob/c42ae922e1abed2720c7fac993777e1bd59c0c93/package/bleparser/sensorpush.py

MIT License applies.
"""
from __future__ import annotations

import logging

from bluetooth_data_tools import short_address
from bluetooth_sensor_state_data import BluetoothData
from home_assistant_bluetooth import BluetoothServiceInfo
from sensor_state_data import SensorLibrary
from sensor_state_data.description import BaseSensorDescription

_LOGGER = logging.getLogger(__name__)

SENSORPUSH_DEVICE_TYPES = {1: "HT1", 64: "HTP.xw", 65: "HT.w"}

SENSORPUSH_MANUFACTURER_DATA_LEN = {
    3: "HT.w",
    5: "HTP.xw",
}

LOCAL_NAMES = ["HTP.xw", "HT.w"]

SENSORPUSH_SERVICE_UUID_HT1 = "ef090000-11d6-42ba-93b8-9dd7ec090aa9"
SENSORPUSH_SERVICE_UUID_V2 = "ef090000-11d6-42ba-93b8-9dd7ec090ab0"

SENSORPUSH_PACK_PARAMS = {
    64: [[-40.0, 140.0, 0.0025], [0.0, 100.0, 0.0025], [30000.0, 125000.0, 1.0]],
    65: [[-40.0, 125.0, 0.0025], [0.0, 100.0, 0.0025]],
}

SENSORPUSH_DATA_TYPES = {
    1: [SensorLibrary.TEMPERATURE__CELSIUS, SensorLibrary.HUMIDITY__PERCENTAGE],
    64: [
        SensorLibrary.TEMPERATURE__CELSIUS,
        SensorLibrary.HUMIDITY__PERCENTAGE,
        SensorLibrary.PRESSURE__MBAR,
    ],
    65: [SensorLibrary.TEMPERATURE__CELSIUS, SensorLibrary.HUMIDITY__PERCENTAGE],
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


def determine_device_type(
    service_info: BluetoothServiceInfo, manufacturer_data: dict[int, bytes]
) -> str | None:
    """Determine the device type based on the name and UUID"""
    local_name = service_info.name

    if local_name == "s" and SENSORPUSH_SERVICE_UUID_HT1 in service_info.service_uuids:
        return "HT1"

    device_type = None
    for match_name in LOCAL_NAMES:
        if match_name in local_name:
            device_type = match_name

    if not device_type and SENSORPUSH_SERVICE_UUID_V2 in service_info.service_uuids:
        first_manufacturer_data_value_len = len(next(iter(manufacturer_data.values())))
        return SENSORPUSH_MANUFACTURER_DATA_LEN.get(first_manufacturer_data_value_len)

    return device_type


class SensorPushBluetoothDeviceData(BluetoothData):
    """Date update for SensorPush Bluetooth devices."""

    def _start_update(self, service_info: BluetoothServiceInfo) -> None:
        """Update from BLE advertisement data."""
        manufacturer_data = service_info.manufacturer_data
        if not manufacturer_data:
            return

        result = {}
        device_type = determine_device_type(service_info, manufacturer_data)
        if not device_type:
            return

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
