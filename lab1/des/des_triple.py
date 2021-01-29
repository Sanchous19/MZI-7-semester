from des.des import decrypt, encrypt


def encrypt_triple(message, key1, key2, key3):
    return encrypt(decrypt(encrypt(message, key1), key2), key3)


def decrypt_triple(message, key1, key2, key3):
    return decrypt(encrypt(decrypt(message, key3), key2), key1)
