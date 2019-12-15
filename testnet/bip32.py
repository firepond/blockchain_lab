import hashlib
import hmac
import struct
import ecdsa

from secp256k1 import PrivateKey
from binascii import hexlify, unhexlify
from ecdsa.ecdsa import int_to_string, string_to_int
from ecdsa.curves import SECP256k1
from ecdsa.numbertheory import square_root_mod_prime as sqrt_mod

MIN_ENTROPY_LEN = 128        # bits
BIP32_HARDEN    = 0x80000000 # choose from hardened set of child keys
CURVE_GEN       = ecdsa.ecdsa.generator_secp256k1
CURVE_ORDER     = CURVE_GEN.order()
FIELD_ORDER     = SECP256k1.curve.p()
INFINITY        = ecdsa.ellipticcurve.INFINITY


def privateToPublic(privateKey):
  if(type(privateKey) == str):
    privateKey = unhexlify(privateKey)
  privkey = PrivateKey(privateKey)
  compressed = privkey.pubkey.serialize()
  # uncompressed = hexlify(privkey.pubkey.serialize(compressed=False)).decode('ascii')
  # print(compressed)
  # print(uncompressed)
  return compressed


def childKeyDerivationPrivate(masterPrivateKey, masterChaincode, index):
  i_str = ser32(index)
  if index & BIP32_HARDEN:
    data = bytes.fromhex("00") + masterPrivateKey + bytes(i_str)
  else:
    data = privateToPublic(masterPrivateKey) + bytes(i_str)
  (Il, Ir) = hmacsha512(data, masterChaincode)
  ilInt =  string_to_int(Il)
  if ilInt > CURVE_ORDER:
    return None
  privateInt = string_to_int(masterPrivateKey)
  priavteKeyInt = (ilInt + privateInt) % CURVE_ORDER
  if (priavteKeyInt == 0):
    return None
  secret = (b'\0'*32 + int_to_string(priavteKeyInt))[-32:]
  return secret, Ir
        
    

# Generate a seed byte sequence S of a chosen length (between 128 and 512 bits; 256 bits is advised) from a (P)RNG.
# Calculate I = HMAC-SHA512(Key = "Bitcoin seed", Data = S)
# Split I into two 32-byte sequences, IL and IR.
# Use parse256(IL) as master secret key, and IR as master chain code.
def generateMainKey(entropy):
  seed = entropy
  # seed = hashlib.sha256(entropy).digest()
  key = b"Bitcoin seed"
  i = hmacsha512(seed, key)
  return i

def hmacsha512(text, key):
  result = hmac.new(key, text, digestmod=hashlib.sha512).digest()
  return (result[:32], result[32:])


  
def ser32(integer):
  return struct.pack(">L", integer)

def main():
  # testSeed = bytes.fromhex("fffcf9f6f3f0edeae7e4e1dedbd8d5d2cfccc9c6c3c0bdbab7b4b1aeaba8a5a29f9c999693908d8a8784817e7b7875726f6c696663605d5a5754514e4b484542")
  testSeed =  hashlib.sha256(bytes(1723119)).digest()
  # root = bytes.fromhex("17231195")
  (masterPrivateKey, masterChainCode) = generateMainKey(testSeed)
  
  

  masterPublicKey = privateToPublic(masterPrivateKey)
  key0 = childKeyDerivationPrivate(masterPrivateKey, masterChainCode, 2147483647+BIP32_HARDEN)
  print(key0[0].hex())
  print(privateToPublic(key0[0]).hex())
  print(key0[1].hex())


    
    


if __name__ == "__main__":
  main()
