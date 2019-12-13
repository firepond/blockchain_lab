# !/usr/bin/env python

import sys
py_version = sys.version_info.major
N = 115792089237316195423570985008687907852837564279074904382605163141518161494337
G = (55066263022277343669578718895168534326250603453777594175500187360389116729240,
     32670510020758816978083085130507043184471273380659243275938904335757337482424)

SIGHASH_ALL = 1
SIGHASH_NONE = 2
SIGHASH_SINGLE = 3
SIGHASH_ANYONECANPAY = 129

version_dict = {
    "scripthash": {
        "main": "0x05",
        "testnet": "0xc4"
    },
    "pubkeyhash": {
        "main": "0x00",
        "testnet": "0x6f"
    },
    "main": {
        "scripthash": "0x05",
        "pubkeyhash": "0x00"
    },
    "testnet": {
        "scripthash": "0xc4",
        "pubkeyhash": "0x6f"
    }
}

op_dict = {
    "OP_FALSE": "0x00",
    "OP_TRUE": "0x51",

    "OP_PUSHDATA1": "0x4c",
    "OP_PUSHDATA1": "0x4d",
    "OP_PUSHDATA1": "0x4e",

    "OP_0": "0x00",
    "OP_1": "0x51",
    "OP_2": "0x52",
    "OP_3": "0x53",
    "OP_4": "0x54",
    "OP_5": "0x55",
    "OP_6": "0x56",
    "OP_7": "0x57",
    "OP_8": "0x58",
    "OP_9": "0x59",
    "OP_10": "0x5a",
    "OP_11": "0x5b",
    "OP_12": "0x5c",
    "OP_13": "0x5d",
    "OP_14": "0x5e",
    "OP_15": "0x5f",
    "OP_16": "0x60",

    "OP_IF": "0x63",
    "OP_NOTIF": "0x64",
    "OP_ELSE": "0x67",
    "OP_ENDIF": "0x68",
    "OP_VERIFY": "0x69",
    "OP_RETURN": "0x6a",

    "OP_DROP": "0x75",
    "OP_DUP": "0x76",
    "OP_SWAP": "0x7c",

    "OP_EQUAL": "0x87",
    "OP_EQUALVERIFY": "0x88",

    "OP_RIPEMD160": "0xa6",
    "OP_SHA1": "0xa7",
    "OP_SHA256": "0xa8",
    "OP_HASH160": "0xa9",
    "OP_HASH256": "0xaa",
    "OP_CHECKSIG": "0xac",
    "OP_CHECKSIGVERIFY": "0xad",
    "OP_CHECKMULTISIG": "0xae",
    "OP_CHECKMULTISIGVERIFY": "0xaf",

    "OP_CHECKLOCKTIMEVERIFY": "0xb1",
    "OP_CHECKSEQUENCEVERIFY": "0xb2",

}

code_strings = {
    2: '01',
    10: '0123456789',
    16: '0123456789abcdef',
    32: 'abcdefghijklmnopqrstuvwxyz234567',
    58: '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
}

if py_version == 3:
    code_strings[256] = ''.join([chr(x) for x in range(256)])
else:
    code_strings[256] = ''.join([chr(x) for x in xrange(256)])
