# Advertisement format

SensorPush has published a [GATT API](https://www.sensorpush.com/bluetooth-api)
but not an advertisement specification, so everything below is reverse
engineered. Each claim states where it comes from: the packet captures
committed in `tests/test_parser.py`, or a statement from SensorPush.

Correct it rather than trust it. If you have a device that contradicts a table
here, that is a bug report worth filing.

## The manufacturer id carries payload bytes

A SensorPush advertisement puts the first two bytes of its payload in the
_company identifier_ field of the manufacturer-specific data structure. The
value is not a Bluetooth SIG company id; it is data. The full payload is

```text
company_id.to_bytes(2, "little") + manufacturer_data
```

which is what `_find_latest_data()` reconstructs.

Two consequences fall out of this, and both shape the parser:

- Every distinct reading looks to a scanner like a new manufacturer. A host
  that accumulates manufacturer data per device — as HA's Bluetooth stack does
  — ends up holding one entry per advertisement it has heard. The committed
  HTP.xw capture holds 256.
- The newest reading is therefore the most recently _added_ entry, not a fixed
  key. The parser looks at `changed_manufacturer_data` and walks it in reverse.

## Payload header (v2 devices)

Byte 0 of the payload is a header:

| bits | meaning                                          |
| ---- | ------------------------------------------------ |
| 0–1  | page id                                          |
| 2–7  | device type index; device type id = `64 + index` |

Verified across the committed captures: every entry of a capture yields the same
device type id — 31 of 31 frames for the HT.w, 256 of 256 for the HTP.xw —
including the frames that are not page 0.

| device type id | model  | manufacturer data bytes | payload bytes |
| -------------- | ------ | ----------------------- | ------------- |
| 64             | HTP.xw | 5                       | 7             |
| 65             | HT.w   | 3                       | 5             |
| 66             | TC.x   | 2 or 3 — see below      | 4 or 5        |

The local name is a weaker signal than the header: it is absent on passive
scans, and it is user-editable in the SensorPush app. The manufacturer data
length is weaker still — HT.w and TC.x can both advertise 3 bytes.

### Pages

Only two pages have been observed on v2 devices:

| page | content                                                 |
| ---- | ------------------------------------------------------- |
| 0    | the current sensor reading; changes every advertisement |
| 3    | a static frame, one per device                          |

Pages 1 and 2 have not been seen on a v2 capture.

The page 3 frame is byte-identical across capture batches taken minutes apart,
while page 0 changes continuously:

| model  | page 3 payload         |
| ------ | ---------------------- |
| HT.w   | `07 2c fe 00 01`       |
| HTP.xw | `03 45 ad 00 01 00 00` |

Its header parses consistently with page 0 (`0x07 >> 2` → 65, `0x03 >> 2` → 64),
so it is a real protocol page and not noise. What the bytes mean is unknown —
bytes 1–2 differ per model, and `00 01` appears at the same offset in both. It
is **not** battery: the SensorPush lead developer
[stated](https://github.com/Bluetooth-Devices/sensorpush-ble/issues/28#issuecomment-2402606715)
that battery information is not broadcast at all and is only readable over
GATT. The parser discards every page but 0.

## Packed values (v2 devices)

Payload bytes 1 onwards are one little-endian unsigned integer holding all
fields in mixed radix, least significant field first. Each field `i` covers

```text
count_i = int((max_i - min_i) / step_i + step_i / 2) + 1
```

consecutive values, and is read back as

```text
value_i = (packed % (count_0 * ... * count_i)) // (count_0 * ... * count_i-1)
          * step_i + min_i
```

| model  | field            | min   | max    | step   | values |
| ------ | ---------------- | ----- | ------ | ------ | ------ |
| HTP.xw | temperature (°C) | -40   | 140    | 0.0025 | 72001  |
|        | humidity (%)     | 0     | 100    | 0.0025 | 40001  |
|        | pressure (Pa)    | 30000 | 125000 | 1      | 95001  |
| HT.w   | temperature (°C) | -40   | 125    | 0.0025 | 66001  |
|        | humidity (%)     | 0     | 100    | 0.0025 | 40001  |
| TC.x   | temperature (°C) | -200  | 1800   | 0.0625 | 32001  |

Pressure is advertised in pascals and reported in hPa.

### The payload is wider than the value space

The product of the field counts is the number of payloads the format can
actually produce. Nothing constrains a corrupt or foreign advertisement to stay
inside it, and a packed integer above the product wraps the outermost modulus
into a plausible-looking reading rather than an obviously broken one:

| model  | encodable payloads  | payload bits     | share of the space used |
| ------ | ------------------- | ---------------- | ----------------------- |
| HTP.xw | 273 613 520 207 001 | 48               | 97.2%                   |
| HT.w   | 2 640 106 001       | 32               | 61.5%                   |
| TC.x   | 32 001              | 32 (3-byte form) | 0.0007%                 |

So a range check on the packed integer is worth far more than it looks, and
almost entirely because of TC.x.

### How many bytes a TC.x sends

The two answers in the vendor-authored PR that
[added TC.x support](https://github.com/Bluetooth-Devices/sensorpush-ble/pull/33)
disagree: `SENSORPUSH_MANUFACTURER_DATA_LEN` declares 2 bytes, its test
advertisements carry 3. The PR predates the hardware, so neither is a
confirmed wire length.

A single 15-bit field fits in either. The parser therefore requires only the
bytes the fields need — a header byte plus 2 — instead of an observed
advertisement length, so both shapes decode. A capture from real TC.x hardware
would settle it.

## HT1

The HT1 is an older, unrelated format. It shares no header encoding with the v2
devices: applying `64 + (byte0 >> 2)` to an HT1 capture yields a different
"device type" almost every frame.

- 2 bytes of manufacturer data, so a 4-byte payload.
- Identified by the service UUID `ef090000-11d6-42ba-93b8-9dd7ec090aa9` together
  with the local name `s`, which is what every HT1 seen so far advertises.
- The model marker is in byte 3: `(payload[3] & 124) >> 2 == 1`.
- Humidity is `payload[0] | (payload[1] & 0x0F) << 8`, temperature is
  `payload[1] >> 4 | payload[2] << 4 | (payload[3] & 0x03) << 12`, both
  converted with the Sensirion SHT2x formulas:
  `-6 + 125 * raw / 2^12` and `-46.85 + 175.72 * raw / 2^14`.
- It also emits an iBeacon frame under Apple's company id 76, carrying the HT1
  service UUID as the proximity UUID. It holds no sensor data.

## Battery

Not in the advertisement, on any model. Reading it requires a GATT connection —
see [#28](https://github.com/Bluetooth-Devices/sensorpush-ble/issues/28).
