#!/usr/bin/python # -*- coding: UTF-8 -*-
import base58
import hashlib
import common

def publickey_to_address(public_key):
    versionbytes = "6f"
  
    key1 = common.bin_ripemd160(common.bin_sha256(public_key))
    # key1 = common.bin_ripemd160(public_key)
    print("key1:" + key1)
    key2 = common.bin_sha256(common.bin_sha256(versionbytes+key1))
    print("key2:"+key2)
    check = key2[0:8]
    print(check)
    key3 = versionbytes + key1 + check
    print("key3:"+key3)
    result = base58.b58encode_int(int(key3, 16))
    return result


print("hello")
pk = "02fcc4d9733749cd7f5746465e370bd9e089c1b354555c966cea1b826c6589d999"
address = publickey_to_address(pk)
print(address)
