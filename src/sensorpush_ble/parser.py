"""Parser for SensorPush BLE advertisements.

This file is shamelessly copied from the following repository:
https://github.com/Ernst79/bleparser/blob/c42ae922e1abed2720c7fac993777e1bd59c0c93/package/bleparser/sensorpush.py

MIT License applies.
"""

from __future__ import annotations

import logging

from bluetooth_data_tools import short_address
from bluetooth_sensor_state_data import BluetoothData
from habluetooth import BluetoothServiceInfoBleak
from sensor_state_data import SensorLibrary
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

_TYPE_IDS = {model: type_id for type_id, model in SENSORPUSH_DEVICE_TYPES.items()}

# Minimum length, in bytes, of the reconstructed advertisement payload
# (2-byte manufacturer id + manufacturer data) needed to decode every field
# of a given device type. Shorter payloads are truncated or corrupt and would
# otherwise decode to plausible-looking but wrong values. Derived from the
# advertised manufacturer data lengths so the two cannot drift apart; the HT1
# is not in that table and its decoder reads up to byte 3.
SENSORPUSH_MIN_DATA_LEN = {1: 4} | {
    _TYPE_IDS[model]: mfg_data_len + 2
    for mfg_data_len, model in SENSORPUSH_MANUFACTURER_DATA_LEN.items()
}


def _packed_fields(
    type_id: int,
) -> tuple[tuple[BaseSensorDescription, int, int, float, float], ...]:
    """Precompute the (type, modulus, divisor, step, minimum) of each packed field.

    The moduli and divisors only depend on the pack parameters, so they are
    computed once at import instead of on every advertisement.
    """
    fields = []
    modulus = 1
    for (min_value, max_value, step), data_type in zip(
        SENSORPUSH_PACK_PARAMS[type_id], SENSORPUSH_DATA_TYPES[type_id]
    ):
        divisor = modulus
        modulus *= int((max_value - min_value) / step + step / 2.0) + 1
        fields.append((data_type, modulus, divisor, step, min_value))
    return tuple(fields)


SENSORPUSH_PACKED_FIELDS = {
    type_id: _packed_fields(type_id) for type_id in SENSORPUSH_PACK_PARAMS
}


def _device_type_id(data: bytes) -> int:
    """Return the device type id encoded in the first byte of a v2 payload."""
    return 64 + (data[0] >> 2)


def _find_latest_data(
    manufacturer_data: dict[int, bytes], is_ht1: bool
) -> bytes | None:
    for id_ in reversed(manufacturer_data):
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
    min_len = SENSORPUSH_MIN_DATA_LEN.get(device_type_id)
    if min_len is None:
        # A model this library does not know about is not an error condition,
        # and every one of its advertisements would repeat the message.
        _LOGGER.debug("SensorPush device type id %s unknown", device_type_id)
        return {}

    if len(mfg_data) < min_len:
        _LOGGER.debug(
            "Truncated data for SensorPush device type id %s: %s bytes, expected %s",
            device_type_id,
            len(mfg_data),
            min_len,
        )
        return {}

    if device_type_id == 1:
        return decode_ht1_values(mfg_data)

    packed_values = int.from_bytes(mfg_data[1:], "little")

    values = {}
    for data_type, modulus, divisor, step, min_value in SENSORPUSH_PACKED_FIELDS[
        device_type_id
    ]:
        value = round(packed_values % modulus // divisor * step + min_value, 2)
        if data_type is SensorLibrary.PRESSURE__MBAR:
            value = value / 100.0
        values[data_type] = value

    return values


def _is_ht1(service_info: BluetoothServiceInfoBleak) -> bool:
    """Return True if the advertisement comes from an HT1."""
    # The name of the HT1s seems to always be "s"
    return (
        service_info.name == "s"
        and SENSORPUSH_SERVICE_UUID_HT1 in service_info.service_uuids
    )


def _name_device_type(local_name: str) -> str | None:
    """Return the device type advertised in the local name, if any."""
    device_type: str | None = None
    for match_name, model_name in LOCAL_NAMES.items():
        if match_name in local_name:
            device_type = model_name
    return device_type


def determine_device_type(
    manufacturer_data: dict[int, bytes],
    data: bytes | None,
    name_device_type: str | None,
) -> str | None:
    """Determine the device type based on the payload, the name and the data length"""
    # The model is encoded in every page 0 payload, which is more reliable than
    # the local name (absent on passive scans, and stale on devices renamed in
    # the app) and than the manufacturer data length (HT.w and TC.x share one).
    if data and (
        payload_device_type := SENSORPUSH_DEVICE_TYPES.get(_device_type_id(data))
    ):
        return payload_device_type

    if name_device_type:
        return name_device_type

    first_manufacturer_data_value_len = len(next(iter(manufacturer_data.values())))
    return SENSORPUSH_MANUFACTURER_DATA_LEN.get(first_manufacturer_data_value_len)


class SensorPushBluetoothDeviceData(BluetoothData):
    """Date update for SensorPush Bluetooth devices."""

    def _start_update(self, service_info: BluetoothServiceInfoBleak) -> None:
        """Update from BLE advertisement data."""
        manufacturer_data = service_info.manufacturer_data
        if not manufacturer_data:
            return

        ht1 = _is_ht1(service_info)
        name_device_type = None if ht1 else _name_device_type(service_info.name)
        if (
            not ht1
            and not name_device_type
            and SENSORPUSH_SERVICE_UUID_V2 not in service_info.service_uuids
        ):
            return

        changed_manufacturer_data = self.changed_manufacturer_data(service_info)
        # If len(changed_manufacturer_data) > 1 it means we switched ble adapters
        # so we do not know which data is the latest: the advertisement can still
        # identify the device, but we need to wait for the next update to decode
        # values from it.
        decodable = len(changed_manufacturer_data) == 1
        # Scanning for the page 0 payload is the expensive part of handling an
        # advertisement, so do it once and use the result for both the model
        # and the values.
        data = _find_latest_data(
            changed_manufacturer_data if decodable else manufacturer_data, ht1
        )

        device_type = (
            "HT1"
            if ht1
            else determine_device_type(manufacturer_data, data, name_device_type)
        )
        if not device_type:
            return

        self.set_device_type(device_type)
        self.set_device_manufacturer("SensorPush")

        name = service_info.name.removeprefix("SensorPush ")
        if not name or ht1:
            name = f"{device_type} {short_address(service_info.address)}"
        self.set_device_name(name)

        if not (data and decodable):
            return

        values = decode_values(data, 1 if ht1 else _device_type_id(data))
        for data_type, value in values.items():
            self.update_predefined_sensor(data_type, value)
