from uuid import UUID

from bleak.backends.device import BLEDevice
from bluetooth_data_tools import monotonic_time_coarse
from bluetooth_sensor_state_data import DeviceClass, SensorUpdate
from habluetooth import BluetoothServiceInfoBleak
from sensor_state_data import (
    DeviceKey,
    SensorDescription,
    SensorDeviceClass,
    SensorDeviceInfo,
    SensorValue,
    Units,
)

from sensorpush_ble.parser import SensorPushBluetoothDeviceData


def make_bluetooth_service_info(  # noqa: PLR0913
    name: str,
    manufacturer_data: dict[int, bytes],
    service_uuids: list[str],
    address: str,
    rssi: int,
    service_data: dict[UUID, bytes],
    source: str,
    tx_power: int = 0,
    raw: bytes | None = None,
) -> BluetoothServiceInfoBleak:
    return BluetoothServiceInfoBleak(
        name=name,
        manufacturer_data=manufacturer_data,
        service_uuids=service_uuids,
        address=address,
        rssi=rssi,
        service_data=service_data,
        source=source,
        device=BLEDevice(
            name=name,
            address=address,
            details={},
            rssi=rssi,
        ),
        time=monotonic_time_coarse(),
        advertisement=None,
        connectable=True,
        tx_power=tx_power,
        raw=raw,
    )


HTW_DETECT_CHANGED_1 = make_bluetooth_service_info(
    name="",
    manufacturer_data={
        28932: b"\x03\xe0G",
        11271: b"\xfe\x00\x01",
        39940: b"\xb4\rA",
        5380: b"\xaeD>",
        11012: b"\x8d\xc0>",
        9476: b"\x95\x1b=",
        54788: b"\xab'=",
        2820: b"\n\xea=",
        14084: b"\xa6\xb2=",
        54532: b"\x8f\x18=",
        40708: b"\x0f_=",
        56324: b"\x8e\x17=",
        49156: b"_\xfd<",
        43012: b"9\xe8<",
        11268: b"+\xe0<",
        22020: b"\x8d\x16=",
        50692: b"j\x03=",
        31748: b"l\x04=",
        63492: b"\x83\x11=",
        3332: b"\xc76=",
        37636: b"\x8e\x17=",
        42756: b"x\x0b=",
        9732: b"\xad(=",
        1284: b"\x99\x1d=",
        10756: b"v\n=",
        12548: b"k\x04=",
        21764: b"U\xf8<",
        43780: b"=\xeb<",
        3588: b"C\xee<",
        42500: b"2\xe5<",
        3844: b"$\xdd<",
    },
    service_uuids=["ef090000-11d6-42ba-93b8-9dd7ec090ab0"],
    rssi=-53,
    address="aa:bb:cc:dd:ee:ff",
    service_data={},
    source="local",
)

HTW_DETECT_CHANGED_2 = make_bluetooth_service_info(
    name="",
    manufacturer_data={
        28932: b"\x03\xe0G",
        11271: b"\xfe\x00\x01",
        39940: b"\xb4\rA",
        5380: b"\xaeD>",
        11012: b"\x8d\xc0>",
        9476: b"\x95\x1b=",
        54788: b"\xab'=",
        2820: b"\n\xea=",
        14084: b"\xa6\xb2=",
        54532: b"\x8f\x18=",
        40708: b"\x0f_=",
        56324: b"\x8e\x17=",
        49156: b"_\xfd<",
        43012: b"9\xe8<",
        11268: b"+\xe0<",
        22020: b"\x8d\x16=",
        50692: b"j\x03=",
        31748: b"l\x04=",
        63492: b"\x83\x11=",
        3332: b"\xc76=",
        37636: b"\x8e\x17=",
        42756: b"x\x0b=",
        9732: b"\xad(=",
        1284: b"\x99\x1d=",
        10756: b"v\n=",
        12548: b"k\x04=",
        21764: b"U\xf8<",
        43780: b"=\xeb<",
        3588: b"C\xee<",
        42500: b"2\xe5<",
        3844: b"$\xdd<",
        14596: b"6\xe7<",
    },
    service_uuids=["ef090000-11d6-42ba-93b8-9dd7ec090ab0"],
    rssi=-52,
    address="aa:bb:cc:dd:ee:ff",
    service_data={},
    source="local",
)

HTPW_DETECT_CHANGE_1 = make_bluetooth_service_info(
    name="",
    rssi=-60,
    manufacturer_data={
        17667: b"\xad\x00\x01\x00\x00",
        1280: b"\xe7\xb4\xe1\xaf\xb6",
        2304: b"7\xe1:\xb7\xb6",
        55552: b"#\xc7$\xad\xb6",
        58624: b";\x01%\x9d\xb6",
        44288: b"\xa2|'x\xb6",
        64000: b";\xad\xdc\xa7\xb6",
        28672: b"\xdb\xe8\\\xa2\xb6",
        7168: b"\xb5\xbd\xe0\xaf\xb6",
        11264: b"\x00S}\xae\xb6",
        4096: b"\xe9\xef\x8e\xba\xb6",
        44800: b"\x85\xa2=\xb5\xb6",
        32768: b"\x86b\xe9\xc1\xb6",
        37376: b"\x8bS<\xc1\xb6",
        25344: b"\xb4\xb2\xe7\xbb\xb6",
        51200: b"\xae\xdc\xc8\x97\xb6",
        49152: b"O\x80O\xc7\xb6",
        17664: b"\x0e\xb7q\xa0\xb6",
        34816: b"\x9a\xf6\xf8\xc3\xb6",
        21760: b"G\xd9\xd6\xa7\xb6",
        512: b"\xaa\x14M\xc5\xb6",
        41984: b"\xfd\xb4\xd7\xa5\xb6",
        16640: b"\x9b\xdd\xd9\xa5\xb6",
        33024: b"\x99\xdbB\xb9\xb6",
        25088: b"\xee\xec\xea\xbf\xb6",
        24576: b"\xc3G\x16\x99\xb6",
        50176: b"\x88Q\x9d\xc4\xb6",
        57856: b"~\x1a\xb0\x87\xb6",
        2816: b"08\xa2\xc4\xb6",
        19712: b",\xf1u\x9a\xb6",
        26880: b"\x8f\x0f(\xa9\xb6",
        54528: b"U\xbe\x1c\x9b\xb6",
        7936: b"\x01\x1e\x93\xbc\xb6",
        52992: b"R\x19\xb9\x91\xb6",
        9472: b"\x0f\xb9\x9a\x87\xb6",
        47360: b"A\xe16\xb5\xb6",
        14080: b"r\x82S\xc7\xb6",
        60416: b"#A\xc5v\xb6",
        19968: b"\xf5=\x80\xa0\xb6",
        30976: b"\r\x99\x13\x91\xb6",
        9216: b'\x08">\xbd\xb6',
        16896: b'"\x94L\xc7\xb6',
        54784: b"\xae\xce%\x9d\xb6",
        21248: b"\xb9\xe9\xe1\xb9\xb6",
        40960: b"\x15}\xda\xbb\xb6",
        16128: b"s\xe9\xf7\xc5\xb6",
        36608: b"\xad\xd6\x8f\xc0\xb6",
        1536: b"\x1a\xd1\x8c\xb0\xb6",
        30720: b"\xf4`\x93\xb4\xb6",
        17920: b"mIi\xae\xb6",
        30464: b"\x8c}\x19\x99\xb6",
        61952: b"\xb4{\xec\xbd\xb6",
        30208: b'\xa8\xac"\x9b\xb6',
        27904: b"D\xcb8\xb5\xb6",
        45568: b"\xfc\xb5\xdf\xa9\xb6",
        12288: b"\xe9\x11\xa7\x8f\xb6",
        6400: b"\\\xcf\xe0\xb7\xb6",
        10496: b"P_\xe1\xbb\xb6",
        52736: b"fv\xd3\xa1\xb6",
        37888: b"\xb1\x7f'\xaf\xb6",
        6656: b"\x80Wh\x90\xb6",
        15872: b"\xd7\x91\xe0\xb7\xb6",
        28160: b"P<\xc5\x95\xb6",
        37632: b"NN\xc7x\xb6",
        11776: b"\x03z0\xab\xb6",
        48896: b"B\x9e\xaa\xc8\xb6",
        65280: b"w\xb1\xee\xb9\xb6",
        56320: b"\xb1\xfa\x1f\x99\xb6",
        59136: b"_\xd5\x1c\x97\xb6",
        26368: b"\xbe\x82\xbd\x93\xb6",
        7424: b"A\xc8\x19\x99\xb6",
        49408: b"\xef\xda\x91\xb4\xb6",
        24832: b"l\xc03\xbd\xb6",
        48128: b"Vs4\xa9\xb6",
        48384: b"\xack;\xbb\xb6",
        20224: b"\xd8O\xe5\xb9\xb6",
        35840: b"Nj\xe1\xbb\xb6",
        51712: b"\x96\xba\xcc\x9b\xb6",
        23296: b"\xda\\v\x9c\xb6",
        39168: b"0j\xe3\xb3\xb6",
        29440: b"\xf9\xc9J\xc3\xb6",
        54016: b"\xe9\x1c\x88\xa6\xb6",
        62208: b"\x1b\x0f\xe3\xbf\xb6",
        33280: b"\xc2s\x83\xa2\xb6",
        20480: b"\xa9\xc5\xc4\x95\xb6",
        50688: b"\xd5O\xe5\xb7\xb6",
        19456: b"T }\x9e\xb6",
        27136: b"\xd3\n\xda\xbb\xb6",
        34304: b"\x10\x164\xb7\xb6",
        3328: b'"\xb1\x1c\x99\xb6',
        50944: b"it\xbf\x91\xb6",
        29952: b"\xd7\xc5\xb8\x93\xb6",
        46592: b"\x14-\xbc\x95\xb6",
        60928: b"|\xcd\xb8\x8d\xb6",
        16384: b"4\x95\xce\x9b\xb6",
        23040: b"\x99\xca\x9f\x8d\xb6",
        58112: b"P\xcc;\xb7\xb6",
        22784: b"\x8a4L\xc5\xb6",
        12800: b"el\xe0\xad\xb6",
        8960: b"xe\x8e\xb8\xb6",
        13568: b"\xec2\x8f\xb8\xb6",
        36864: b"\r\xde1\xb5\xb6",
        64512: b"\xf7\xf8\x17n\xb6",
        39424: b"?\xbc\x87\xa8\xb6",
        8448: b"\xfa\x8c\xa6\x8f\xb6",
        53760: b"\xf3\x92\xdd\xb3\xb6",
        23552: b"A\xb5A\xc3\xb6",
        51968: b"\xb6\xc9\xa5^\xb6",
        9728: b"\xff\xa1\x7f\xa6\xb6",
        18944: b"\xc0\xddI\xc1\xb6",
        46848: b"\x05t\xea\xb9\xb6",
        33792: b"\xdb\xa8\xd9\xa3\xb6",
        6144: b"+\xcb?\xb9\xb6",
        10752: b";\x93:\xb9\xb6",
        40704: b"\x8e\x85p\x96\xb6",
        58368: b"\x91\xf2\xd0\x9d\xb6",
        32512: b"\xec\x80\x85\xa4\xb6",
        55808: b"-\x98\x80\xb0\xb6",
        25856: b"\x90\xd5\x85\xaa\xb6",
        58880: b":J\x81\xba\xb6",
        31232: b"\x80\xfe\xdd\xa5\xb6",
        55040: b"o13\xa9\xb6",
        50432: b"t\xe5I\xc3\xb6",
        37120: b"\xd3\x05\x89\xa6\xb6",
        12544: b"\x06\x00<\xbd\xb6",
        59904: b"\xddb\xbe\x93\xb6",
        27392: b"OB\x0f\x8f\xb6",
        61696: b"\x1d\xe8\x18\x97\xb6",
        29696: b"#\xcc\xde\xbd\xb6",
        32000: b"X}3\xb5\xb6",
        44544: b"\xb8\xa1\x1e\x99\xb6",
        7680: b"\xe7Qr\x98\xb6",
        45312: b"\xfbI\x10\x8f\xb6",
        63488: b"\xc6\xda(\xa5\xb6",
        25600: b"O\xda\xe2\xb7\xb6",
        24320: b"r\x14n\x98\xb6",
        62464: b"\xb0\x87\xf4\xc1\xb6",
        63744: b"\x96\xd6\x14\x95\xb6",
        21504: b"[\x85\x0f\x93\xb6",
        8192: b"\xb7\x84\xd3\xa5\xb6",
        29184: b"\xbf\xdfg\x90\xb6",
        64768: b"\xa2\x84\xe5\xbf\xb6",
        57088: b"9\t\x8a\xb4\xb6",
        22272: b"r~(\x9f\xb6",
        55296: b".\x03\xc6\x97\xb6",
        34560: b"\xb5r\x7f\xa0\xb6",
        52224: b"\xe2\xc3\x1c\xa3\xb6",
        13824: b"8>\xe6\xb5\xb6",
        46080: b"Y\x7f@\xb9\xb6",
        34048: b"/_k\x96\xb6",
        4608: b"9\x95K\xc3\xb6",
        62720: b"K-;\x84\xb6",
        44032: b"\xd5\xd0\xa7\xc6\xb6",
        35584: b"?}D\xcd\xb6",
        43008: b"2\x8f\x8a\xae\xb6",
        47104: b"\xa1\xff\xe6\xbb\xb6",
        61184: b"\xa3\x7f%\xa5\xb6",
        59648: b"\xf1\xb8\x8d\xb4\xb6",
        57344: b"\x88\xee2\xb7\xb6",
        36096: b"\\\xd5\x9c\xc0\xb6",
        38912: b"n\x12_\x90\xb6",
        56832: b"$gG\xc3\xb6",
        18176: b"\xf9\x96\xfc\xc5\xb6",
        18432: b"b\xcdA\xbf\xb6",
        57600: b":\x19@\xbf\xb6",
        18688: b"$\xe2\xcb\x99\xb6",
        38656: b"\x0cA-\xb9\xb6",
        48640: b"V\x8c\xda\xab\xb6",
        46336: b'"WL]\xb6',
        9984: b"\xa8\xab\xa2\xd2\xb6",
        42496: b"4\x0b\x1f\x9b\xb6",
        41216: b")M%\xab\xb6",
        49664: b"M%6\xa9\xb6",
        42240: b",\x1e\x86\xb6\xb6",
        20992: b"\xab\x052\xbd\xb6",
        53504: b"\x8a\xf6\x84\xaa\xb6",
        56064: b"\xda\xbf\xa4`\xb6",
        53248: b"\x18:\xc8\x99\xb6",
        19200: b"\xb1\xb4\x89\xbc\xb6",
        38400: b"\xba=\x1f\x99\xb6",
        41728: b"\xe4\xa3+\xb1\xb6",
        5376: b"z\xd6\x94\xb2\xb6",
        47616: b"\x88\x1f\xe3\xb9\xb6",
        60672: b"\x9c\x85{\xb4\xb6",
        3584: b"\xe7\xdc\xa8\xc6\xb6",
        28416: b"\xdc\xddT\x90\xb6",
        14336: b"\x87\xa6\xf2\xc5\xb6",
        43776: b"9y\x8a\xae\xb6",
        39936: b"\xe2\x8cSa\xb6",
        5632: b"\xa5_0\xab\xb6",
        14592: b"\xbf\xa9\x80\xae\xb6",
        63232: b"\xd6A\xc5\x99\xb6",
        13312: b"=\xcdL\xc3\xb6",
        8704: b"\xf9\xd1'\xa1\xb6",
        11008: b"\xdc\xed\xf6\xc5\xb6",
        26624: b"\x9b\x81\xc2\x99\xb6",
        13056: b"\x88@\xda\xab\xb6",
        5888: b"p\xea\x85\xaa\xb6",
        12032: b"L\xdb\xe9\xb9\xb6",
        3072: b"$\x1e\x83\xac\xb6",
        31744: b"\xcb\xe60\xad\xb6",
        14848: b"\xee\x9d\xe8\xc9\xb6",
        45824: b"Mo\x8e\xb2\xb6",
        768: b"\xa6\x8d=\xb5\xb6",
        56576: b"\x02\xba\x8d\xb0\xb6",
        49920: b"\xa3\xac$\x9d\xb6",
        41472: b"\x9dM\xe0\xab\xb6",
        65024: b"\x89!\xf2\xbf\xb6",
        1024: b"\x89\xbf\x8d\xb4\xb6",
        0: b"\xb6\xc5\xc2\x97\xb6",
        61440: b"\xad\xa8s\x98\xb6",
        17408: b"\xc2\x99?\xbb\xb6",
        42752: b"R\xf81\xa9\xb6",
        38144: b'\x83\x89"\x9d\xb6',
        43520: b"\xb7\xa2'\x9f\xb6",
        35328: b";d\xa2\xd0\xb6",
        51456: b"\xa4\x85h\x90\xb6",
        35072: b"\xfb\x90@\xbf\xb6",
        39680: b"\xf5\xcb\x04\xa1\xb6",
        4352: b"j\xd0e\x92\xb6",
        32256: b"\xcc\x99\xbf\x95\xb6",
        3840: b"\xd0\xdd\xc7\x99\xb6",
        45056: b"U\xf2\xf0\xc3\xb6",
        47872: b'\xdc\x07"\x9b\xb6',
        60160: b"0\x8a\xdf\xbb\xb6",
        28928: b"\xe7\xa8\xdc\xaf\xb6",
        54272: b"c\x15\x85\xb4\xb6",
        17152: b"\xc0Q\x7f\xa0\xb6",
        5120: b"B@w\x9a\xb6",
        43264: b"rC\x85\xaa\xb6",
        23808: b"[\xe3=\xb7\xb6",
        256: b"\x9c\x9f\x90\xb2\xb6",
        6912: b"\xf2\x18\xdc\xab\xb6",
        15616: b"\x1b,/\xb5\xb6",
        15104: b"{=\xbf\x91\xb6",
        4864: b"g?\xe3\xb9\xb6",
        36352: b"\x88\xac2\xad\xb6",
        22016: b"O\x91\x18\x95\xb6",
        52480: b"q\x8dS\xc9\xb6",
        62976: b"ZX\x7f\xa2\xb6",
        59392: b"\xef\xdc\xa5\xc4\xb6",
        15360: b"\xd0\x9aD\xc1\xb6",
        10240: b"a\x92\x92\xb0\xb6",
        2048: b" /]\x9a\xb6",
        20736: b"\x9d\xdek\x94\xb6",
        2560: b"\xf5z=\xb3\xb6",
        22528: b"j@\xe2\xad\xb6",
        26112: b"\x18\x1f\xc5x\xb6",
        40448: b"\xdf\xfe=\xbb\xb6",
        11520: b"2\xf7<\xbb\xb6",
        1792: b"$\n\x1c\x99\xb6",
        40192: b"\xaa\x88\xff\xc9\xb6",
        27648: b"\x87\xac\xb8\x8d\xb6",
        33536: b"{:\x1b\x97\xb6",
        64256: b"B\r.\xa9\xb6",
        31488: b"\x98\xfa\xb6\x91\xb6",
    },
    service_uuids=["ef090000-11d6-42ba-93b8-9dd7ec090ab0"],
    address="aa:bb:cc:dd:ee:ff",
    service_data={},
    source="local",
)
HTPW_DETECT_CHANGE_2 = make_bluetooth_service_info(
    name="",
    rssi=-60,
    manufacturer_data={
        17667: b"\xad\x00\x01\x00\x00",
        24064: b"6[:\xbb\xb6",
        1280: b"\xe7\xb4\xe1\xaf\xb6",
        2304: b"7\xe1:\xb7\xb6",
        55552: b"#\xc7$\xad\xb6",
        58624: b";\x01%\x9d\xb6",
        44288: b"\xa2|'x\xb6",
        64000: b";\xad\xdc\xa7\xb6",
        28672: b"\xdb\xe8\\\xa2\xb6",
        7168: b"\xb5\xbd\xe0\xaf\xb6",
        11264: b"\x00S}\xae\xb6",
        4096: b"\xe9\xef\x8e\xba\xb6",
        44800: b"\x85\xa2=\xb5\xb6",
        32768: b"\x86b\xe9\xc1\xb6",
        37376: b"\x8bS<\xc1\xb6",
        25344: b"\xb4\xb2\xe7\xbb\xb6",
        51200: b"\xae\xdc\xc8\x97\xb6",
        49152: b"O\x80O\xc7\xb6",
        17664: b"\x0e\xb7q\xa0\xb6",
        34816: b"\x9a\xf6\xf8\xc3\xb6",
        21760: b"G\xd9\xd6\xa7\xb6",
        512: b"\xaa\x14M\xc5\xb6",
        41984: b"\xfd\xb4\xd7\xa5\xb6",
        16640: b"\x9b\xdd\xd9\xa5\xb6",
        33024: b"\x99\xdbB\xb9\xb6",
        25088: b"\xee\xec\xea\xbf\xb6",
        24576: b"\xc3G\x16\x99\xb6",
        50176: b"\x88Q\x9d\xc4\xb6",
        57856: b"~\x1a\xb0\x87\xb6",
        2816: b"08\xa2\xc4\xb6",
        19712: b",\xf1u\x9a\xb6",
        26880: b"\x8f\x0f(\xa9\xb6",
        54528: b"U\xbe\x1c\x9b\xb6",
        7936: b"\x01\x1e\x93\xbc\xb6",
        52992: b"R\x19\xb9\x91\xb6",
        9472: b"\x0f\xb9\x9a\x87\xb6",
        47360: b"A\xe16\xb5\xb6",
        14080: b"r\x82S\xc7\xb6",
        60416: b"#A\xc5v\xb6",
        19968: b"\xf5=\x80\xa0\xb6",
        30976: b"\r\x99\x13\x91\xb6",
        9216: b'\x08">\xbd\xb6',
        16896: b'"\x94L\xc7\xb6',
        54784: b"\xae\xce%\x9d\xb6",
        21248: b"\xb9\xe9\xe1\xb9\xb6",
        40960: b"\x15}\xda\xbb\xb6",
        16128: b"s\xe9\xf7\xc5\xb6",
        36608: b"\xad\xd6\x8f\xc0\xb6",
        1536: b"\x1a\xd1\x8c\xb0\xb6",
        30720: b"\xf4`\x93\xb4\xb6",
        17920: b"mIi\xae\xb6",
        30464: b"\x8c}\x19\x99\xb6",
        61952: b"\xb4{\xec\xbd\xb6",
        30208: b'\xa8\xac"\x9b\xb6',
        27904: b"D\xcb8\xb5\xb6",
        45568: b"\xfc\xb5\xdf\xa9\xb6",
        12288: b"\xe9\x11\xa7\x8f\xb6",
        6400: b"\\\xcf\xe0\xb7\xb6",
        10496: b"P_\xe1\xbb\xb6",
        52736: b"fv\xd3\xa1\xb6",
        37888: b"\xb1\x7f'\xaf\xb6",
        6656: b"\x80Wh\x90\xb6",
        15872: b"\xd7\x91\xe0\xb7\xb6",
        28160: b"P<\xc5\x95\xb6",
        37632: b"NN\xc7x\xb6",
        11776: b"\x03z0\xab\xb6",
        48896: b"B\x9e\xaa\xc8\xb6",
        65280: b"w\xb1\xee\xb9\xb6",
        56320: b"\xb1\xfa\x1f\x99\xb6",
        59136: b"_\xd5\x1c\x97\xb6",
        26368: b"\xbe\x82\xbd\x93\xb6",
        7424: b"A\xc8\x19\x99\xb6",
        49408: b"\xef\xda\x91\xb4\xb6",
        24832: b"l\xc03\xbd\xb6",
        48128: b"Vs4\xa9\xb6",
        48384: b"\xack;\xbb\xb6",
        20224: b"\xd8O\xe5\xb9\xb6",
        35840: b"Nj\xe1\xbb\xb6",
        51712: b"\x96\xba\xcc\x9b\xb6",
        23296: b"\xda\\v\x9c\xb6",
        39168: b"0j\xe3\xb3\xb6",
        29440: b"\xf9\xc9J\xc3\xb6",
        54016: b"\xe9\x1c\x88\xa6\xb6",
        62208: b"\x1b\x0f\xe3\xbf\xb6",
        33280: b"\xc2s\x83\xa2\xb6",
        20480: b"\xa9\xc5\xc4\x95\xb6",
        50688: b"\xd5O\xe5\xb7\xb6",
        19456: b"T }\x9e\xb6",
        27136: b"\xd3\n\xda\xbb\xb6",
        34304: b"\x10\x164\xb7\xb6",
        3328: b'"\xb1\x1c\x99\xb6',
        50944: b"it\xbf\x91\xb6",
        29952: b"\xd7\xc5\xb8\x93\xb6",
        46592: b"\x14-\xbc\x95\xb6",
        60928: b"|\xcd\xb8\x8d\xb6",
        16384: b"4\x95\xce\x9b\xb6",
        23040: b"\x99\xca\x9f\x8d\xb6",
        58112: b"P\xcc;\xb7\xb6",
        22784: b"\x8a4L\xc5\xb6",
        12800: b"el\xe0\xad\xb6",
        8960: b"xe\x8e\xb8\xb6",
        13568: b"\xec2\x8f\xb8\xb6",
        36864: b"\r\xde1\xb5\xb6",
        64512: b"\xf7\xf8\x17n\xb6",
        39424: b"?\xbc\x87\xa8\xb6",
        8448: b"\xfa\x8c\xa6\x8f\xb6",
        53760: b"\xf3\x92\xdd\xb3\xb6",
        23552: b"A\xb5A\xc3\xb6",
        51968: b"\xb6\xc9\xa5^\xb6",
        9728: b"\xff\xa1\x7f\xa6\xb6",
        18944: b"\xc0\xddI\xc1\xb6",
        46848: b"\x05t\xea\xb9\xb6",
        33792: b"\xdb\xa8\xd9\xa3\xb6",
        6144: b"+\xcb?\xb9\xb6",
        10752: b";\x93:\xb9\xb6",
        40704: b"\x8e\x85p\x96\xb6",
        58368: b"\x91\xf2\xd0\x9d\xb6",
        32512: b"\xec\x80\x85\xa4\xb6",
        55808: b"-\x98\x80\xb0\xb6",
        25856: b"\x90\xd5\x85\xaa\xb6",
        58880: b":J\x81\xba\xb6",
        31232: b"\x80\xfe\xdd\xa5\xb6",
        55040: b"o13\xa9\xb6",
        50432: b"t\xe5I\xc3\xb6",
        37120: b"\xd3\x05\x89\xa6\xb6",
        12544: b"\x06\x00<\xbd\xb6",
        59904: b"\xddb\xbe\x93\xb6",
        27392: b"OB\x0f\x8f\xb6",
        61696: b"\x1d\xe8\x18\x97\xb6",
        29696: b"#\xcc\xde\xbd\xb6",
        32000: b"X}3\xb5\xb6",
        44544: b"\xb8\xa1\x1e\x99\xb6",
        7680: b"\xe7Qr\x98\xb6",
        45312: b"\xfbI\x10\x8f\xb6",
        63488: b"\xc6\xda(\xa5\xb6",
        25600: b"O\xda\xe2\xb7\xb6",
        24320: b"r\x14n\x98\xb6",
        62464: b"\xb0\x87\xf4\xc1\xb6",
        63744: b"\x96\xd6\x14\x95\xb6",
        21504: b"[\x85\x0f\x93\xb6",
        8192: b"\xb7\x84\xd3\xa5\xb6",
        29184: b"\xbf\xdfg\x90\xb6",
        64768: b"\xa2\x84\xe5\xbf\xb6",
        57088: b"9\t\x8a\xb4\xb6",
        22272: b"r~(\x9f\xb6",
        55296: b".\x03\xc6\x97\xb6",
        34560: b"\xb5r\x7f\xa0\xb6",
        52224: b"\xe2\xc3\x1c\xa3\xb6",
        13824: b"8>\xe6\xb5\xb6",
        46080: b"Y\x7f@\xb9\xb6",
        34048: b"/_k\x96\xb6",
        4608: b"9\x95K\xc3\xb6",
        62720: b"K-;\x84\xb6",
        44032: b"\xd5\xd0\xa7\xc6\xb6",
        35584: b"?}D\xcd\xb6",
        43008: b"2\x8f\x8a\xae\xb6",
        47104: b"\xa1\xff\xe6\xbb\xb6",
        61184: b"\xa3\x7f%\xa5\xb6",
        59648: b"\xf1\xb8\x8d\xb4\xb6",
        57344: b"\x88\xee2\xb7\xb6",
        36096: b"\\\xd5\x9c\xc0\xb6",
        38912: b"n\x12_\x90\xb6",
        56832: b"$gG\xc3\xb6",
        18176: b"\xf9\x96\xfc\xc5\xb6",
        18432: b"b\xcdA\xbf\xb6",
        57600: b":\x19@\xbf\xb6",
        18688: b"$\xe2\xcb\x99\xb6",
        38656: b"\x0cA-\xb9\xb6",
        48640: b"V\x8c\xda\xab\xb6",
        46336: b'"WL]\xb6',
        9984: b"\xa8\xab\xa2\xd2\xb6",
        42496: b"4\x0b\x1f\x9b\xb6",
        41216: b")M%\xab\xb6",
        49664: b"M%6\xa9\xb6",
        42240: b",\x1e\x86\xb6\xb6",
        20992: b"\xab\x052\xbd\xb6",
        53504: b"\x8a\xf6\x84\xaa\xb6",
        56064: b"\xda\xbf\xa4`\xb6",
        53248: b"\x18:\xc8\x99\xb6",
        19200: b"\xb1\xb4\x89\xbc\xb6",
        38400: b"\xba=\x1f\x99\xb6",
        41728: b"\xe4\xa3+\xb1\xb6",
        5376: b"z\xd6\x94\xb2\xb6",
        47616: b"\x88\x1f\xe3\xb9\xb6",
        60672: b"\x9c\x85{\xb4\xb6",
        3584: b"\xe7\xdc\xa8\xc6\xb6",
        28416: b"\xdc\xddT\x90\xb6",
        14336: b"\x87\xa6\xf2\xc5\xb6",
        43776: b"9y\x8a\xae\xb6",
        39936: b"\xe2\x8cSa\xb6",
        5632: b"\xa5_0\xab\xb6",
        14592: b"\xbf\xa9\x80\xae\xb6",
        63232: b"\xd6A\xc5\x99\xb6",
        13312: b"=\xcdL\xc3\xb6",
        8704: b"\xf9\xd1'\xa1\xb6",
        11008: b"\xdc\xed\xf6\xc5\xb6",
        26624: b"\x9b\x81\xc2\x99\xb6",
        13056: b"\x88@\xda\xab\xb6",
        5888: b"p\xea\x85\xaa\xb6",
        12032: b"L\xdb\xe9\xb9\xb6",
        3072: b"$\x1e\x83\xac\xb6",
        31744: b"\xcb\xe60\xad\xb6",
        14848: b"\xee\x9d\xe8\xc9\xb6",
        45824: b"Mo\x8e\xb2\xb6",
        768: b"\xa6\x8d=\xb5\xb6",
        56576: b"\x02\xba\x8d\xb0\xb6",
        49920: b"\xa3\xac$\x9d\xb6",
        41472: b"\x9dM\xe0\xab\xb6",
        65024: b"\x89!\xf2\xbf\xb6",
        1024: b"\x89\xbf\x8d\xb4\xb6",
        0: b"\xb6\xc5\xc2\x97\xb6",
        61440: b"\xad\xa8s\x98\xb6",
        17408: b"\xc2\x99?\xbb\xb6",
        42752: b"R\xf81\xa9\xb6",
        38144: b'\x83\x89"\x9d\xb6',
        43520: b"\xb7\xa2'\x9f\xb6",
        35328: b";d\xa2\xd0\xb6",
        51456: b"\xa4\x85h\x90\xb6",
        35072: b"\xfb\x90@\xbf\xb6",
        39680: b"\xf5\xcb\x04\xa1\xb6",
        4352: b"j\xd0e\x92\xb6",
        32256: b"\xcc\x99\xbf\x95\xb6",
        3840: b"\xd0\xdd\xc7\x99\xb6",
        45056: b"U\xf2\xf0\xc3\xb6",
        47872: b'\xdc\x07"\x9b\xb6',
        60160: b"0\x8a\xdf\xbb\xb6",
        28928: b"\xe7\xa8\xdc\xaf\xb6",
        54272: b"c\x15\x85\xb4\xb6",
        17152: b"\xc0Q\x7f\xa0\xb6",
        5120: b"B@w\x9a\xb6",
        43264: b"rC\x85\xaa\xb6",
        23808: b"[\xe3=\xb7\xb6",
        256: b"\x9c\x9f\x90\xb2\xb6",
        6912: b"\xf2\x18\xdc\xab\xb6",
        15616: b"\x1b,/\xb5\xb6",
        15104: b"{=\xbf\x91\xb6",
        4864: b"g?\xe3\xb9\xb6",
        36352: b"\x88\xac2\xad\xb6",
        22016: b"O\x91\x18\x95\xb6",
        52480: b"q\x8dS\xc9\xb6",
        62976: b"ZX\x7f\xa2\xb6",
        59392: b"\xef\xdc\xa5\xc4\xb6",
        15360: b"\xd0\x9aD\xc1\xb6",
        10240: b"a\x92\x92\xb0\xb6",
        2048: b" /]\x9a\xb6",
        20736: b"\x9d\xdek\x94\xb6",
        2560: b"\xf5z=\xb3\xb6",
        22528: b"j@\xe2\xad\xb6",
        26112: b"\x18\x1f\xc5x\xb6",
        40448: b"\xdf\xfe=\xbb\xb6",
        11520: b"2\xf7<\xbb\xb6",
        1792: b"$\n\x1c\x99\xb6",
        40192: b"\xaa\x88\xff\xc9\xb6",
        27648: b"\x87\xac\xb8\x8d\xb6",
        33536: b"{:\x1b\x97\xb6",
        64256: b"B\r.\xa9\xb6",
        31488: b"\x98\xfa\xb6\x91\xb6",
    },
    service_uuids=["ef090000-11d6-42ba-93b8-9dd7ec090ab0"],
    address="aa:bb:cc:dd:ee:ff",
    service_data={},
    source="local",
)

HT1_DETECT_CHANGED_1 = make_bluetooth_service_info(
    name="s",
    manufacturer_data={
        2061: b"b\x05",
        76: b"\x02\x15\xef\t\x00\x00\x11\xd6B\xba"
        + b"\x93\xb8\x9d\xd7\xec\t\n\xa9\x00\x01\tV\xc8",
        2060: b"b\x05",
        6156: b"b\x05",
        2059: b"b\x05",
        6155: b"b\x05",
        6154: b"b\x05",
        2058: b"b\x05",
        2057: b"b\x05",
        63498: b"a\x05",
        63499: b"a\x05",
        63500: b"a\x05",
        63501: b"a\x05",
        63502: b"a\x05",
        59407: b"a\x05",
        63503: b"a\x05",
        63504: b"a\x05",
        59409: b"a\x05",
        59410: b"a\x05",
        59411: b"a\x05",
        59412: b"a\x05",
        59413: b"a\x05",
        59414: b"a\x05",
        55319: b"a\x05",
        55320: b"a\x05",
        55321: b"a\x05",
        55322: b"a\x05",
        55323: b"a\x05",
        55324: b"a\x05",
        55325: b"a\x05",
        51229: b"a\x05",
        51230: b"a\x05",
        51231: b"a\x05",
        51232: b"a\x05",
        51233: b"a\x05",
        47138: b"a\x05",
        47139: b"a\x05",
        47140: b"a\x05",
        47141: b"a\x05",
        43045: b"a\x05",
        43046: b"a\x05",
        43047: b"a\x05",
        43048: b"a\x05",
        38952: b"a\x05",
        43049: b"a\x05",
        38954: b"a\x05",
        43050: b"a\x05",
        38955: b"a\x05",
        38956: b"a\x05",
        38957: b"a\x05",
        38958: b"a\x05",
        34863: b"a\x05",
        34864: b"a\x05",
        34865: b"a\x05",
        34866: b"a\x05",
        34867: b"a\x05",
        30772: b"a\x05",
        30773: b"a\x05",
        30774: b"a\x05",
        30775: b"a\x05",
        30776: b"a\x05",
        30777: b"a\x05",
        26682: b"a\x05",
        26683: b"a\x05",
        26684: b"a\x05",
        26685: b"a\x05",
        26686: b"a\x05",
    },
    service_data={},
    service_uuids=["ef090000-11d6-42ba-93b8-9dd7ec090aa9"],
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    source="local",
)

HT1_DETECT_CHANGED_2 = make_bluetooth_service_info(
    name="s",
    manufacturer_data={
        2061: b"b\x05",
        76: b"\x02\x15\xef\t\x00\x00\x11\xd6B\xba"
        + b"\x93\xb8\x9d\xd7\xec\t\n\xa9\x00\x01\tV\xc8",
        2060: b"b\x05",
        6156: b"b\x05",
        2059: b"b\x05",
        6155: b"b\x05",
        6154: b"b\x05",
        2058: b"b\x05",
        2057: b"b\x05",
        63498: b"a\x05",
        63499: b"a\x05",
        63500: b"a\x05",
        63501: b"a\x05",
        63502: b"a\x05",
        59407: b"a\x05",
        63503: b"a\x05",
        63504: b"a\x05",
        59409: b"a\x05",
        59410: b"a\x05",
        59411: b"a\x05",
        59412: b"a\x05",
        59413: b"a\x05",
        59414: b"a\x05",
        55319: b"a\x05",
        55320: b"a\x05",
        55321: b"a\x05",
        55322: b"a\x05",
        55323: b"a\x05",
        55324: b"a\x05",
        55325: b"a\x05",
        51229: b"a\x05",
        51230: b"a\x05",
        51231: b"a\x05",
        51232: b"a\x05",
        51233: b"a\x05",
        47138: b"a\x05",
        47139: b"a\x05",
        47140: b"a\x05",
        47141: b"a\x05",
        43045: b"a\x05",
        43046: b"a\x05",
        43047: b"a\x05",
        43048: b"a\x05",
        38952: b"a\x05",
        43049: b"a\x05",
        38954: b"a\x05",
        43050: b"a\x05",
        38955: b"a\x05",
        38956: b"a\x05",
        38957: b"a\x05",
        38958: b"a\x05",
        34863: b"a\x05",
        34864: b"a\x05",
        34865: b"a\x05",
        34866: b"a\x05",
        34867: b"a\x05",
        30772: b"a\x05",
        30773: b"a\x05",
        30774: b"a\x05",
        30775: b"a\x05",
        30776: b"a\x05",
        30777: b"a\x05",
        26682: b"a\x05",
        26683: b"a\x05",
        26684: b"a\x05",
        26685: b"a\x05",
        26686: b"a\x05",
        26687: b"a\x05",
    },
    service_data={},
    service_uuids=["ef090000-11d6-42ba-93b8-9dd7ec090aa9"],
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    source="local",
)


def test_can_create():
    SensorPushBluetoothDeviceData()


def test_ht_w():
    parser = SensorPushBluetoothDeviceData()
    service_info = make_bluetooth_service_info(
        name="SensorPush HT.w 0CA1",
        manufacturer_data={39428: b"\xc9\xa5F"},
        service_data={},
        service_uuids=["ef090000-11d6-42ba-93b8-9dd7ec090ab0"],
        address="aa:bb:cc:dd:ee:ff",
        rssi=-60,
        source="local",
    )
    result = parser.update(service_info)
    assert result == SensorUpdate(
        title=None,
        devices={
            None: SensorDeviceInfo(
                name="HT.w 0CA1",
                model="HT.w",
                manufacturer="SensorPush",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=DeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=DeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
            DeviceKey(key="humidity", device_id=None): SensorDescription(
                device_key=DeviceKey(key="humidity", device_id=None),
                device_class=DeviceClass.HUMIDITY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
        },
        entity_values={
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=20.53,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=44.9,
            ),
        },
    )


def test_ht_w_raw():
    parser = SensorPushBluetoothDeviceData()
    service_info = make_bluetooth_service_info(
        name="SensorPush HT.w 0CA1",
        manufacturer_data={1: b""},  # anything here
        service_data={},
        service_uuids=["ef090000-11d6-42ba-93b8-9dd7ec090ab0"],
        address="aa:bb:cc:dd:ee:ff",
        rssi=-60,
        source="local",
        raw=b"\x06\xff\x04\x9a\xc9\xa5\x46",
    )
    result = parser.update(service_info)
    assert result == SensorUpdate(
        title=None,
        devices={
            None: SensorDeviceInfo(
                name="HT.w 0CA1",
                model="HT.w",
                manufacturer="SensorPush",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=DeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=DeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
            DeviceKey(key="humidity", device_id=None): SensorDescription(
                device_key=DeviceKey(key="humidity", device_id=None),
                device_class=DeviceClass.HUMIDITY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
        },
        entity_values={
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=20.53,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=44.9,
            ),
        },
    )


def test_ht_w_page_zero_data_first():
    parser = SensorPushBluetoothDeviceData()
    service_info = make_bluetooth_service_info(
        name="SensorPush HT.w 0CA1",
        manufacturer_data={29956: b"SdF"},
        service_data={},
        service_uuids=["ef090000-11d6-42ba-93b8-9dd7ec090ab0"],
        address="aa:bb:cc:dd:ee:ff",
        rssi=-60,
        source="local",
    )
    result = parser.update(service_info)
    assert result == SensorUpdate(
        title=None,
        devices={
            None: SensorDeviceInfo(
                name="HT.w 0CA1",
                model="HT.w",
                manufacturer="SensorPush",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="humidity", device_id=None): SensorDescription(
                device_key=DeviceKey(key="humidity", device_id=None),
                device_class=DeviceClass.HUMIDITY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=DeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=DeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
        },
        entity_values={
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=44.73,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=20.48,
            ),
        },
    )


def test_ht_w_large_data_set():
    parser = SensorPushBluetoothDeviceData()
    result = parser.update(HTW_DETECT_CHANGED_1)
    assert result == SensorUpdate(
        title=None,
        devices={
            None: SensorDeviceInfo(
                name="HT.w EEFF",
                model="HT.w",
                manufacturer="SensorPush",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            )
        },
        entity_values={
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-53,
            )
        },
        binary_entity_descriptions={},
        binary_entity_values={},
        events={},
    )

    result2 = parser.update(HTW_DETECT_CHANGED_2)

    assert result2 == SensorUpdate(
        title=None,
        devices={
            None: SensorDeviceInfo(
                name="HT.w EEFF",
                model="HT.w",
                manufacturer="SensorPush",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="humidity", device_id=None): SensorDescription(
                device_key=DeviceKey(key="humidity", device_id=None),
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=20.44,
            ),
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=38.7,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-52,
            ),
        },
        binary_entity_descriptions={},
        binary_entity_values={},
        events={},
    )


def test_htp_w_large_data_set():
    parser = SensorPushBluetoothDeviceData()
    result = parser.update(HTPW_DETECT_CHANGE_1)
    assert result == SensorUpdate(
        title=None,
        devices={
            None: SensorDeviceInfo(
                name="HTP.xw EEFF",
                model="HTP.xw",
                manufacturer="SensorPush",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            )
        },
        entity_values={
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            )
        },
        binary_entity_descriptions={},
        binary_entity_values={},
        events={},
    )
    result2 = parser.update(HTPW_DETECT_CHANGE_2)
    assert result2 == SensorUpdate(
        title=None,
        devices={
            None: SensorDeviceInfo(
                name="HTP.xw EEFF",
                model="HTP.xw",
                manufacturer="SensorPush",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="humidity", device_id=None): SensorDescription(
                device_key=DeviceKey(key="humidity", device_id=None),
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="pressure", device_id=None): SensorDescription(
                device_key=DeviceKey(key="pressure", device_id=None),
                device_class=SensorDeviceClass.PRESSURE,
                native_unit_of_measurement=Units.PRESSURE_MBAR,
            ),
        },
        entity_values={
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=22.3,
            ),
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=52.81,
            ),
            DeviceKey(key="pressure", device_id=None): SensorValue(
                device_key=DeviceKey(key="pressure", device_id=None),
                name="Pressure",
                native_value=997.59,
            ),
        },
        binary_entity_descriptions={},
        binary_entity_values={},
        events={},
    )


def test_ht1():
    parser = SensorPushBluetoothDeviceData()
    service_info = make_bluetooth_service_info(
        name="s",
        manufacturer_data={18484: b"b\x05"},
        service_data={},
        service_uuids=["ef090000-11d6-42ba-93b8-9dd7ec090aa9"],
        address="aa:bb:cc:dd:ee:ff",
        rssi=-60,
        source="local",
    )
    result = parser.update(service_info)
    assert result == SensorUpdate(
        title=None,
        devices={
            None: SensorDeviceInfo(
                name="HT1 EEFF",
                model="HT1",
                manufacturer="SensorPush",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="humidity", device_id=None): SensorDescription(
                device_key=DeviceKey(key="humidity", device_id=None),
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=58.09,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=13.94,
            ),
        },
    )


def test_ht1_max_value():
    parser = SensorPushBluetoothDeviceData()
    service_info = make_bluetooth_service_info(
        name="s",
        manufacturer_data={65535: b"\xff\x07"},
        service_data={},
        service_uuids=["ef090000-11d6-42ba-93b8-9dd7ec090aa9"],
        address="aa:bb:cc:dd:ee:ff",
        rssi=-60,
        source="local",
    )
    result = parser.update(service_info)
    assert result == SensorUpdate(
        title=None,
        devices={
            None: SensorDeviceInfo(
                name="HT1 EEFF",
                model="HT1",
                manufacturer="SensorPush",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="humidity", device_id=None): SensorDescription(
                device_key=DeviceKey(key="humidity", device_id=None),
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=100.00,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=128.86,
            ),
        },
    )


def test_ht1_min_value():
    parser = SensorPushBluetoothDeviceData()
    service_info = make_bluetooth_service_info(
        name="s",
        manufacturer_data={0: b"\x00\x04"},
        service_data={},
        service_uuids=["ef090000-11d6-42ba-93b8-9dd7ec090aa9"],
        address="aa:bb:cc:dd:ee:ff",
        rssi=-60,
        source="local",
    )
    result = parser.update(service_info)
    assert result == SensorUpdate(
        title=None,
        devices={
            None: SensorDeviceInfo(
                name="HT1 EEFF",
                model="HT1",
                manufacturer="SensorPush",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="humidity", device_id=None): SensorDescription(
                device_key=DeviceKey(key="humidity", device_id=None),
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=0.00,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=-46.85,
            ),
        },
    )


def test_ht1_long_packet_empty():
    parser = SensorPushBluetoothDeviceData()
    service_info = make_bluetooth_service_info(
        name="s",
        manufacturer_data={
            76: b"\x02\x15\xef\t\x00\x00\x11\xd6B\xba\x93"
            + b"\xb8\x9d\xd7\xec\t\n\xa9\x00\x01\tV\xc8"
        },
        service_data={},
        service_uuids=["ef090000-11d6-42ba-93b8-9dd7ec090aa9"],
        address="aa:bb:cc:dd:ee:ff",
        rssi=-60,
        source="local",
    )
    result = parser.update(service_info)
    assert result == SensorUpdate(
        title=None,
        devices={
            None: SensorDeviceInfo(
                name="HT1 EEFF",
                model="HT1",
                manufacturer="SensorPush",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
        },
    )


def test_ht1_large_data_set():
    parser = SensorPushBluetoothDeviceData()
    result = parser.update(HT1_DETECT_CHANGED_1)
    assert parser.supported(HT1_DETECT_CHANGED_1) is True
    assert result == SensorUpdate(
        title=None,
        devices={
            None: SensorDeviceInfo(
                name="HT1 EEFF",
                model="HT1",
                manufacturer="SensorPush",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            )
        },
        entity_values={
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            )
        },
        binary_entity_descriptions={},
        binary_entity_values={},
        events={},
    )

    result2 = parser.update(HT1_DETECT_CHANGED_2)

    assert result2 == SensorUpdate(
        title=None,
        devices={
            None: SensorDeviceInfo(
                name="HT1 EEFF",
                model="HT1",
                manufacturer="SensorPush",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="humidity", device_id=None): SensorDescription(
                device_key=DeviceKey(key="humidity", device_id=None),
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=58.42,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=13.79,
            ),
        },
    )


def test_tcx():
    parser = SensorPushBluetoothDeviceData()
    service_info = make_bluetooth_service_info(
        name="SensorPush TC.x EEFF",
        manufacturer_data={63752: b"\r\x00\x00"},
        service_data={},
        service_uuids=["ef090000-11d6-42ba-93b8-9dd7ec090ab0"],
        address="aa:bb:cc:dd:ee:ff",
        rssi=-60,
        source="local",
    )
    result = parser.update(service_info)
    assert result == SensorUpdate(
        title=None,
        devices={
            None: SensorDeviceInfo(
                name="TC.x EEFF",
                model="TC.x",
                manufacturer="SensorPush",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=23.56,
            ),
        },
    )


def test_tcx_overwriting_mfr_data():
    parser = SensorPushBluetoothDeviceData()
    service_info = make_bluetooth_service_info(
        name="SensorPush TC.x EEFF",
        manufacturer_data={59400: b"\r\x00\x00"},
        service_data={},
        service_uuids=["ef090000-11d6-42ba-93b8-9dd7ec090ab0"],
        address="aa:bb:cc:dd:ee:ff",
        rssi=-60,
        source="local",
    )
    result = parser.update(service_info)
    assert result == SensorUpdate(
        title=None,
        devices={
            None: SensorDeviceInfo(
                name="TC.x EEFF",
                model="TC.x",
                manufacturer="SensorPush",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=22.5,
            ),
        },
    )

    service_info_2 = make_bluetooth_service_info(
        name="SensorPush TC.x EEFF",
        manufacturer_data={59400: b"\r\x00\x00", 63752: b"\r\x03\x00"},
        service_data={},
        service_uuids=["ef090000-11d6-42ba-93b8-9dd7ec090ab0"],
        address="aa:bb:cc:dd:ee:ff",
        rssi=-60,
        source="local",
    )
    result_2 = parser.update(service_info_2)
    assert result_2 == SensorUpdate(
        title=None,
        devices={
            None: SensorDeviceInfo(
                name="TC.x EEFF",
                model="TC.x",
                manufacturer="SensorPush",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=311.19,
            ),
        },
    )

    service_info_3 = make_bluetooth_service_info(
        name="SensorPush TC.x EEFF",
        manufacturer_data={59400: b"\r\x00\x00", 63752: b"\r\x01\x00"},
        service_data={},
        service_uuids=["ef090000-11d6-42ba-93b8-9dd7ec090ab0"],
        address="aa:bb:cc:dd:ee:ff",
        rssi=-60,
        source="local",
    )
    result_3 = parser.update(service_info_3)
    assert result_3 == SensorUpdate(
        title=None,
        devices={
            None: SensorDeviceInfo(
                name="TC.x EEFF",
                model="TC.x",
                manufacturer="SensorPush",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=119.44,
            ),
        },
    )

    service_info_3 = make_bluetooth_service_info(
        name="SensorPush TC.x EEFF",
        manufacturer_data={59400: b"\r\x00\x00", 63752: b"\r\x02\x00"},
        service_data={},
        service_uuids=["ef090000-11d6-42ba-93b8-9dd7ec090ab0"],
        address="aa:bb:cc:dd:ee:ff",
        rssi=-60,
        source="local",
    )
    result_3 = parser.update(service_info_3)
    assert result_3 == SensorUpdate(
        title=None,
        devices={
            None: SensorDeviceInfo(
                name="TC.x EEFF",
                model="TC.x",
                manufacturer="SensorPush",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=215.31,
            ),
        },
    )


def test_tc_detection_active_scans():
    parser = SensorPushBluetoothDeviceData()
    service_info = make_bluetooth_service_info(
        name="SensorPush TC EEFF",
        manufacturer_data={8: b"\x00\x00\x00"},
        service_data={},
        service_uuids=["ef090000-11d6-42ba-93b8-9dd7ec090ab0"],
        address="aa:bb:cc:dd:ee:ff",
        rssi=-60,
        source="local",
    )
    result = parser.update(service_info)
    assert result == SensorUpdate(
        title=None,
        devices={
            None: SensorDeviceInfo(
                name="TC EEFF",
                model="TC.x",
                manufacturer="SensorPush",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=-200.0,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
        },
        binary_entity_descriptions={},
        binary_entity_values={},
        events={},
    )


def test_tc_detection_active_scans_2():
    parser = SensorPushBluetoothDeviceData()
    service_info = make_bluetooth_service_info(
        name="SensorPush TC EEFF",
        manufacturer_data={59400: b"\r\x00\x00"},
        service_data={},
        service_uuids=["ef090000-11d6-42ba-93b8-9dd7ec090ab0"],
        address="aa:bb:cc:dd:ee:ff",
        rssi=-60,
        source="local",
    )
    result = parser.update(service_info)
    assert result == SensorUpdate(
        title=None,
        devices={
            None: SensorDeviceInfo(
                name="TC EEFF",
                model="TC.x",
                manufacturer="SensorPush",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=22.5,
            ),
        },
    )
