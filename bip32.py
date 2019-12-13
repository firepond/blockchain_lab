import hashlib
import hmac
import struct
from secp256k1 import PrivateKey
from binascii import hexlify, unhexlify


def privateToPublic(privateKey):
    privkey = PrivateKey(unhexlify(privateKey))
    compressed = hexlify(privkey.pubkey.serialize()).decode('ascii')
    # uncompressed = hexlify(privkey.pubkey.serialize(compressed=False)).decode('ascii')
    # print(compressed)
    # print(uncompressed)
    return compressed


def childKeyDerivation(parentPriavteKey, parnetChaincode, index):
    BIP32_HARDEN    = 0x80000000

    i_str = struct.pack(">L", index)
    if index & BIP32_HARDEN:
        data = bytes(0) + parentPriavteKey + i_str
    else:
        
    

# Generate a seed byte sequence S of a chosen length (between 128 and 512 bits; 256 bits is advised) from a (P)RNG.
# Calculate I = HMAC-SHA512(Key = "Bitcoin seed", Data = S)
# Split I into two 32-byte sequences, IL and IR.
# Use parse256(IL) as master secret key, and IR as master chain code.
def generateMainKey(magicWord):
    seed = hashlib.sha256(magicWord).digest()
    key = b"Bitcoin seed"
    i = hmacsha512(seed, key)
    return i

def hmacsha512(text, key):
    sign = hmac.new(key, text, digestmod=hashlib.sha512)
    digest = sign.digest()
    privateKey = digest[:32]
    chainCode = digest[32:]
    return privateKey, chainCode

def main():
    testSeed = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
    root = bytes.fromhex("17231195")
    key = generateMainKey(testSeed)
    print(key[0].hex())
    print(key[1].hex())


    
    


if __name__ == "__main__":
    main()

