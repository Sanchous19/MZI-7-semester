from des.des import decrypt, encrypt


def encrypt_double(message, key1, key2):
    return encrypt(encrypt(message, key1), key2)


def decrypt_double(message, key1, key2):
    return decrypt(decrypt(message, key2), key1)
