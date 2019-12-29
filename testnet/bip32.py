import hashlib
import hmac
import struct
import ecdsa
from common_tools import private_to_public
from format_tools import privatekey_to_wif, publickey_to_address


from ecdsa.ecdsa import int_to_string, string_to_int
from ecdsa.curves import SECP256k1
from ecdsa.numbertheory import square_root_mod_prime as sqrt_mod

MIN_ENTROPY_LEN = 128        # bits
BIP32_HARDEN = 0x80000000  # choose from hardened set of child keys
CURVE_GEN = ecdsa.ecdsa.generator_secp256k1
CURVE_ORDER = CURVE_GEN.order()
FIELD_ORDER = SECP256k1.curve.p()
INFINITY = ecdsa.ellipticcurve.INFINITY


def child_key_derivation_from_private(master_private_key, master_chaincode, index):
    i_str = ser32(index)
    if index & BIP32_HARDEN:
        data = bytes.fromhex("00") + master_private_key + bytes(i_str)
    else:
        data = private_to_public(master_private_key) + bytes(i_str)
    (Il, Ir) = hmacsha512(data, master_chaincode)
    ilInt = string_to_int(Il)
    if ilInt > CURVE_ORDER:
        return None
    privateInt = string_to_int(master_private_key)
    priavte_key_int = (ilInt + privateInt) % CURVE_ORDER
    if (priavte_key_int == 0):
        return None
    secret = (b'\0'*32 + int_to_string(priavte_key_int))[-32:]
    print("child key:" + str(index))
    print("private key:" + secret.hex())
    print("wif priavte key:" + privatekey_to_wif(secret))
    publicKey = private_to_public(secret)
    print("public key:" + publicKey.hex())
    print("address:" + publickey_to_address(publicKey))
    print("")
    return secret, Ir


# Generate a seed byte sequence S of a chosen length (between 128 and 512 bits; 256 bits is advised) from a (P)RNG.
# Calculate I = HMAC-SHA512(Key = "Bitcoin seed", Data = S)
# Split I into two 32-byte sequences, IL and IR.
# Use parse256(IL) as master secret key, and IR as master chain code.
def generate_main_key(entropy):
    key = b"Bitcoin seed"
    i = hmacsha512(entropy, key)
    return i


def hmacsha512(text, key):
    result = hmac.new(key, text, digestmod=hashlib.sha512).digest()
    return (result[:32], result[32:])


def ser32(integer):
    return struct.pack(">L", integer)
