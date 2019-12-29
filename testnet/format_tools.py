from common_tools import bin_ripemd160, bin_sha256, b58encode_int

def privatekey_to_wif(private_key):
    if(type(private_key) == str):
        private_key = bytes.fromhex(private_key)
    privatekey_with_prefix = bytes.fromhex("80") + private_key
    hash256 = bin_sha256(bin_sha256(privatekey_with_prefix))

    check = hash256[0:4]
    key3 = (privatekey_with_prefix + check).hex()
    print(key3)
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
