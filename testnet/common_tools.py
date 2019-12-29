import hashlib

from secp256k1 import PrivateKey


def private_to_public(private_key):
    if(type(private_key) == str):
        private_key = bytes.fromhex(private_key)
    private_key_object = PrivateKey(private_key)
    compressed = private_key_object.pubkey.serialize()
    return compressed


def private_to_public_uncompressed(private_key):
    if(type(private_key) == str):
        private_key = bytes.fromhex(private_key)
    private_key_object = PrivateKey(private_key)
    uncompressed = hexlify(private_key_object.pubkey.serialize(
        compressed=False)).decode('ascii')
    return uncompressed


def bin_ripemd160(instr):
    res = hashlib.new("ripemd160")
    res.update(instr)
    return res.digest()


def bin_sha256(instr):
    return hashlib.sha256(instr).digest()


def b58encode_int(i, default_one=True):
    '''Encode an integer using Base58'''
    alphabet = b"123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    if not i and default_one:
        return alphabet[0:1]
    string = b""
    while i:
        i, idx = divmod(i, 58)
        string = alphabet[idx:idx+1] + string
    return string.decode("utf-8")
