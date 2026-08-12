"""Verification of the SensorPush v2 packed-value codec.

The v2 models squeeze every sensor field into a single integer: each field
contributes ``count`` possible steps and is multiplied by the product of the
counts before it. The decoder unpacks that integer with a modulus and a
divisor per field. These tests rebuild the packing side from the published
pack parameters and check that decoding inverts it exactly, including at the
step boundaries where an arithmetic slip would be off by one.
"""

import random

import pytest
from sensor_state_data import SensorLibrary
from sensor_state_data.description import BaseSensorDescription

from sensorpush_ble.parser import (
    SENSORPUSH_DATA_TYPES,
    SENSORPUSH_MIN_DATA_LEN,
    SENSORPUSH_PACK_PARAMS,
    SENSORPUSH_PACKED_FIELDS,
    decode_values,
)

V2_TYPE_IDS = sorted(SENSORPUSH_PACK_PARAMS)


def _step_counts(type_id: int) -> list[int]:
    """Return how many steps each packed field of a device type can hold."""
    return [
        int((max_value - min_value) / step + step / 2.0) + 1
        for min_value, max_value, step in SENSORPUSH_PACK_PARAMS[type_id]
    ]


def _encode(type_id: int, counts: list[int]) -> bytes:
    """Pack per-field step counts the way a SensorPush device does."""
    packed = 0
    divisor = 1
    for count, steps in zip(_step_counts(type_id), counts):
        packed += steps * divisor
        divisor *= count
    payload_len = SENSORPUSH_MIN_DATA_LEN[type_id] - 1
    header = (type_id - 64) << 2
    return bytes([header]) + packed.to_bytes(payload_len, "little")


def _expected(type_id: int, counts: list[int]) -> dict[BaseSensorDescription, float]:
    """Return the reading a device sending those step counts should report."""
    values: dict[BaseSensorDescription, float] = {}
    for (min_value, _, step), data_type, steps in zip(
        SENSORPUSH_PACK_PARAMS[type_id], SENSORPUSH_DATA_TYPES[type_id], counts
    ):
        value = round(steps * step + min_value, 2)
        if data_type is SensorLibrary.PRESSURE__MBAR:
            value = value / 100.0
        values[data_type] = value
    return values


@pytest.mark.parametrize("type_id", V2_TYPE_IDS)
def test_payload_holds_every_encodable_value(type_id: int) -> None:
    """The advertised payload must be wide enough for the whole value space."""
    capacity = SENSORPUSH_PACKED_FIELDS[type_id][-1][1]
    payload_bits = 8 * (SENSORPUSH_MIN_DATA_LEN[type_id] - 1)
    assert capacity <= 1 << payload_bits


@pytest.mark.parametrize("type_id", V2_TYPE_IDS)
def test_round_trip_at_field_extremes(type_id: int) -> None:
    """Every combination of first/second/last step of every field survives."""
    counts = _step_counts(type_id)
    choices = [[0, 1, count // 2, count - 2, count - 1] for count in counts]
    stack: list[list[int]] = [[]]
    for field_choices in choices:
        stack = [taken + [steps] for taken in stack for steps in field_choices]
    for taken in stack:
        assert decode_values(_encode(type_id, taken), type_id) == _expected(
            type_id, taken
        ), taken


def test_round_trip_over_the_whole_tcx_range() -> None:
    """TC.x has a single field, so its entire value space is checkable."""
    for steps in range(_step_counts(66)[0]):
        assert decode_values(_encode(66, [steps]), 66) == _expected(66, [steps])


@pytest.mark.parametrize("type_id", V2_TYPE_IDS)
def test_round_trip_over_random_readings(type_id: int) -> None:
    """Randomly drawn readings decode back to the value that was packed."""
    rand = random.Random(f"sensorpush-{type_id}")
    counts = _step_counts(type_id)
    for _ in range(2000):
        taken = [rand.randrange(count) for count in counts]
        assert decode_values(_encode(type_id, taken), type_id) == _expected(
            type_id, taken
        ), taken


@pytest.mark.parametrize("type_id", V2_TYPE_IDS)
def test_payloads_beyond_the_value_space_are_rejected(type_id: int) -> None:
    """A payload no device could have packed is dropped, not wrapped."""
    capacity = SENSORPUSH_PACKED_FIELDS[type_id][-1][1]
    payload_len = SENSORPUSH_MIN_DATA_LEN[type_id] - 1
    header = bytes([(type_id - 64) << 2])
    for packed in (capacity, capacity + 1, (1 << (8 * payload_len)) - 1):
        data = header + packed.to_bytes(payload_len, "little")
        assert decode_values(data, type_id) == {}


@pytest.mark.parametrize("type_id", V2_TYPE_IDS)
def test_truncated_payloads_are_rejected(type_id: int) -> None:
    """One byte short of the advertised length decodes nothing."""
    counts = _step_counts(type_id)
    data = _encode(type_id, [count // 2 for count in counts])
    assert len(data) == SENSORPUSH_MIN_DATA_LEN[type_id]
    assert decode_values(data[:-1], type_id) == {}
