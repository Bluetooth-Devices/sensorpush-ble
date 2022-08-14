"""Parser for SensorPush BLE advertisements.

This file is shamelessly copied from the following repository:
https://github.com/Ernst79/bleparser/blob/c42ae922e1abed2720c7fac993777e1bd59c0c93/package/bleparser/sensorpush.py

MIT License applies.
"""
from __future__ import annotations

import logging

from bluetooth_sensor_state_data import BluetoothData
from home_assistant_bluetooth import BluetoothServiceInfo
from sensor_state_data import SensorLibrary
from sensor_state_data.description import BaseSensorDescription

_LOGGER = logging.getLogger(__name__)

SENSORPUSH_DEVICE_TYPES = {64: "HTP.xw", 65: "HT.w"}

LOCAL_NAMES = ["HTP.xw", "HT.w"]

SENSORPUSH_PACK_PARAMS = {
    64: [[-40.0, 140.0, 0.0025], [0.0, 100.0, 0.0025], [30000.0, 125000.0, 1.0]],
    65: [[-40.0, 125.0, 0.0025], [0.0, 100.0, 0.0025]],
}

SENSORPUSH_DATA_TYPES = {
    64: [
        SensorLibrary.TEMPERATURE__CELSIUS,
        SensorLibrary.HUMIDITY__PERCENTAGE,
        SensorLibrary.PRESSURE__MBAR,
    ],
    65: [SensorLibrary.TEMPERATURE__CELSIUS, SensorLibrary.HUMIDITY__PERCENTAGE],
}


def _find_latest_data(manufacturer_data: dict[int, bytes]) -> bytes | None:
    for id_ in reversed(list(manufacturer_data)):
        data = int(id_).to_bytes(2, byteorder="little") + manufacturer_data[id_]
        page_id = data[0] & 0x03
        if page_id == 0:
            return data
    return None


def decode_values(
    mfg_data: bytes, device_type_id: int
) -> dict[BaseSensorDescription, float]:
    """Decode values."""
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


class SensorPushBluetoothDeviceData(BluetoothData):
    """Date update for SensorPush Bluetooth devices."""

    def _start_update(self, service_info: BluetoothServiceInfo) -> None:
        """Update from BLE advertisement data."""
        manufacturer_data = service_info.manufacturer_data
        if not manufacturer_data:
            return
        local_name = service_info.name
        result = {}
        device_type = None
        for match_name in LOCAL_NAMES:
            if match_name in local_name:
                device_type = match_name
        if not device_type:
            return
        self.set_device_type(device_type)
        self.set_device_manufacturer("SensorPush")

        changed_manufacturer_data = self.changed_manufacturer_data(service_info)

        if data := _find_latest_data(changed_manufacturer_data):
            device_type_id = 64 + (data[0] >> 2)
            if known_device_type := SENSORPUSH_DEVICE_TYPES.get(device_type_id):
                device_type = known_device_type
            result.update(decode_values(data, device_type_id))

        if service_info.name.startswith("SensorPush "):
            self.set_device_name(service_info.name[11:])
        else:
            self.set_device_name(service_info.name)

        for data_type, value in result.items():
            self.update_predefined_sensor(data_type, value)
