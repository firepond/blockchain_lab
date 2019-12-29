#!/usr/bin/python # -*- coding: UTF-8 -*-
import bip32
import hashlib

import format_tools
import common_tools


def address_test():
    pk_list = ['02b1ebcdbac723f7444fdfb8e83b13bd14fe679c59673a519df6a1038c07b719c6',
               '036e69a3e7c303935403d5b96c47b7c4fa8a80ca569735284a91d930f0f49afa86']
    for pk in pk_list:
        print(format_tools.publickey_to_address(pk))


def wif_test():
    test_seed = hashlib.sha256(bytes(17231195)).digest()
    print("private key:" + test_seed.hex())
    wif = format_tools.privatekey_to_wif(test_seed)
    print("wif:" + wif)


def bip32_test():
    test_seed = hashlib.sha256(bytes(17231195)).digest()
    (master_private_key, master_chaincode) = bip32.generate_main_key(test_seed)

    master_public_key = common_tools.private_to_public(master_private_key)

    print("master private key:" + master_private_key.hex())
    print("master public key:" + master_public_key.hex())
    print("master chaincode:" + master_chaincode.hex())
    print("")

    key0 = bip32.child_key_derivation_from_private(
        master_private_key, master_chaincode, 1)

    key1 = bip32.child_key_derivation_from_private(
        master_private_key, master_chaincode, 2)

    key2 = bip32.child_key_derivation_from_private(
        master_private_key, master_chaincode, 3)

    # key3 = bip32.child_key_derivation_from_private(
    #     master_private_key, master_chaincode, 4)

    key_harden = bip32.child_key_derivation_from_private(
        master_private_key, master_chaincode, 2147483647+bip32.BIP32_HARDEN)


def main():
    # wif_test()
    bip32_test()


if __name__ == "__main__":
    main()
