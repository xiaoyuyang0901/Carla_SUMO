"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class reset_simulation(object):
    __slots__ = ["vehicle_id"]

    __typenames__ = ["string"]

    __dimensions__ = [None]

    def __init__(self):
        self.vehicle_id = ""

    def encode(self):
        buf = BytesIO()
        buf.write(reset_simulation._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        __vehicle_id_encoded = self.vehicle_id.encode('utf-8')
        buf.write(struct.pack('>I', len(__vehicle_id_encoded)+1))
        buf.write(__vehicle_id_encoded)
        buf.write(b"\0")

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != reset_simulation._get_packed_fingerprint():
            raise ValueError("Decode error")
        return reset_simulation._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = reset_simulation()
        __vehicle_id_len = struct.unpack('>I', buf.read(4))[0]
        self.vehicle_id = buf.read(__vehicle_id_len)[:-1].decode('utf-8', 'replace')
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if reset_simulation in parents: return 0
        tmphash = (0xd77125401457135d) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if reset_simulation._packed_fingerprint is None:
            reset_simulation._packed_fingerprint = struct.pack(">Q", reset_simulation._get_hash_recursive([]))
        return reset_simulation._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

