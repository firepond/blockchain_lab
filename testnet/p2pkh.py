import hashlib
from config import version_dict
from base58 import b58encode_int


def hash160(input_bytes):
    sha256_hash = hashlib.sha256(input_bytes).digest()
    ripemd160 = hashlib.new("ripemd160")
    ripemd160.update(sha256_hash)
    return ripemd160.digest()


def hash256(input_bytes):
    hash_1 = hashlib.sha256(input_bytes).digest()
    hash_2 = hashlib.sha256(hash_1).digest()
    return hash_2


def pkh_gen(pk):
    pk_bytes = bytearray.fromhex(pk)
    pk_hash160 = hash160(pk_bytes)
    version = version_dict['testnet']['pubkeyhash']
    version_bytes = bytearray.fromhex(version[2:])
    ver_pk = version_bytes + pk_hash160
    ver_pk_hash256 = hash256(ver_pk)
    check = ver_pk_hash256[:4]
    print("check:" + check)
    ver_pk_check = version_bytes + pk_hash160 + check
    ver_pk_check_int = int.from_bytes(ver_pk_check, 'big')
    output_base58 = b58encode_int(ver_pk_check_int)
    return output_base58


if __name__ == '__main__':
    pk_list = ['02b1ebcdbac723f7444fdfb8e83b13bd14fe679c59673a519df6a1038c07b719c6',
               '036e69a3e7c303935403d5b96c47b7c4fa8a80ca569735284a91d930f0f49afa86']
    for pk in pk_list:
        print(pkh_gen(pk))
    
    print(pkh_gen('17231182'))
