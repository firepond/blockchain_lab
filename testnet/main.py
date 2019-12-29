#!/usr/bin/python # -*- coding: UTF-8 -*-
import hashlib
import bip32


def b58encode_int(i, default_one=True):
    '''Encode an integer using Base58'''
    if not i and default_one:
        return alphabet[0:1]
    string = b""
    while i:
        i, idx = divmod(i, 58)
        string = alphabet[idx:idx+1] + string
    return string


def bin_ripemd160(instr):
    res = hashlib.new("ripemd160")
    res.update(instr)
    return res.digest()


def bin_sha256(instr):
    return hashlib.sha256(instr).digest()


def privatekey_to_wif(privatekey):
    if(type(privatekey) == str):
        privatekey = bytes.fromhex(privatekey)
    privatekey_with_prefix = bytes.fromhex("80") + privatekey
    hash256 = bin_sha256(bin_sha256(privatekey_with_prefix))

    check = hash256[0:4]
    key3 = (privatekey_with_prefix + check).hex()
    result = b58encode_int(int(key3, 16))
    return result


def publickey_to_address(public_key):
    if(type(public_key) == str):
        public_key = bytes.fromhex(public_key)
    version_bytes = bytes.fromhex("6f")
    h160pk = bin_ripemd160(bin_sha256(public_key))
    hash256 = bin_sha256(bin_sha256(version_bytes + h160pk))
    check = hash256[0:4]
    key3 = (version_bytes + h160pk + check).hex()
    result = b58encode_int(int(key3, 16))
    return result




def address_test():
    pk_list = ['02b1ebcdbac723f7444fdfb8e83b13bd14fe679c59673a519df6a1038c07b719c6',
               '036e69a3e7c303935403d5b96c47b7c4fa8a80ca569735284a91d930f0f49afa86']
    for pk in pk_list:
        print(publickey_to_address(pk))


def wif_test():
    test_seed = hashlib.sha256(bytes(17231195)).digest()
    print("private key:" + test_seed.hex())
    wif = privatekey_to_wif(test_seed)
    print("wif:" + str(wif))


def bip32test():
    testSeed = hashlib.sha256(bytes(1723119)).digest()
    # root = bytes.fromhex("17231195")
    (master_private_key, master_chainCode) = generate_main_key(testSeed)

    masterPublicKey = private_to_public(master_private_key)
    key0 = child_key_derivation_from_private(
        master_private_key, master_chainCode, 1)
    # print("private key:" + key0[0].hex())
    # print("public key:" + private_to_public(key0[0]).hex())
    # print(key0[1].hex())
    key1 = child_key_derivation_from_private(
        master_private_key, master_chainCode, 2)
    key1 = child_key_derivation_from_private(
        master_private_key, master_chainCode, 3)
    key1 = child_key_derivation_from_private(
        master_private_key, master_chainCode, 4)


def main():
    # test_seed = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
    # (masterPrivateKey, masterChainCode) = bip32.generateMainKey(test_seed)
    # masterPublicKey = bip32.privateToPublic(masterPrivateKey)
    # print("pvt, hex:", masterPrivateKey.hex())
    # print("pvt, ext:", base58_encode(masterPrivateKey))

    # key0 = bip32.childKeyDerivationPrivate(
    #     masterPrivateKey, masterChainCode, 2147483647+bip32.BIP32_HARDEN)
    # print(key0[0].hex())
    # print(bip32.privateToPublic(key0[0]).hex())
    # print(key0[1].hex())

    # print("private key:" + test_seed.hex())
    # public_key = bip32.privateToPublic(test_seed)
    # print("public key:" + public_key.hex())
    # print(publickey_to_address(public_key))
    address_test()
    wif_test()


if __name__ == "__main__":
    main()
