#!/usr/bin/python # -*- coding: UTF-8 -*-
import base58
import hashlib
import common
import bip32

def publickey_to_address(public_key):
  versionbytes = "6f"  
  key1 = common.bin_ripemd160(common.bin_sha256(public_key))
  # key1 = common.bin_ripemd160(public_key)
  key2 = common.bin_sha256(common.bin_sha256(versionbytes+key1))
  check = key2[0:8]
  key3 = versionbytes + key1 + check
  result = base58.b58encode_int(int(key3, 16))
  return result

def base58encode(text):
  return base58.b58encode_int(int(text.hex(), 16))

def main():
#   testSeed = hashlib.sha256(bytes(1723119)).digest()
  testSeed =  bytes.fromhex("000102030405060708090a0b0c0d0e0f")
  (masterPrivateKey, masterChainCode) = bip32.generateMainKey(testSeed)
  masterPublicKey = bip32.privateToPublic(masterPrivateKey)
  print("pvt, hex:", masterPrivateKey.hex())
  print("pvt, ext:", base58encode(masterPrivateKey))

  key0 = bip32.childKeyDerivationPrivate(masterPrivateKey, masterChainCode, 2147483647+bip32.BIP32_HARDEN)
  print(key0[0].hex())
  print(bip32.privateToPublic(key0[0]).hex())
  print(key0[1].hex())

if __name__ == "__main__":
  main()
