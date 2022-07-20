"""Parser for SensorPush BLE advertisements."""
from __future__ import annotations

from bluetooth_sensor_state_data import SIGNAL_STRENGTH_KEY
from sensor_state_data import DeviceClass, DeviceKey, SensorUpdate
from sensor_state_data.data import (
    ATTR_HW_VERSION,
    ATTR_MANUFACTURER,
    ATTR_MODEL,
    ATTR_NAME,
    ATTR_SW_VERSION,
    SensorDeviceInfo,
)

from .parser import SensorPushBluetoothDeviceData

__version__ = "1.2.2"

__all__ = [
    "SensorPushBluetoothDeviceData",
    "SIGNAL_STRENGTH_KEY",
    "ATTR_HW_VERSION",
    "ATTR_MANUFACTURER",
    "ATTR_MODEL",
    "ATTR_NAME",
    "ATTR_SW_VERSION",
    "SIGNAL_STRENGTH_KEY",
    "SensorDeviceInfo",
    "DeviceClass",
    "DeviceKey",
    "SensorUpdate",
    "SensorDeviceInfo",
]
