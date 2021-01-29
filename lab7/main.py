import ecdsa
import sys
import secrets
import binascii

import encryption


def read_file(file):
    with open(file, 'r') as f:
        return f.read()


def main():
    content = read_file(sys.argv[1])
    b_content = content.encode('utf-8')

    signing_key = ecdsa.SigningKey.generate()
    verifying_key = signing_key.verifying_key
    signature = signing_key.sign(b_content)
    assert verifying_key.verify(signature, b_content)

    print('signing key:', signing_key.to_string())
    print('verifying key:', verifying_key.to_string(), end='\n\n')
    print(content, end='\n\n')
    print(signature, end='\n\n')
    print('-----------------------------------------------', end='\n\n')

    private_key = secrets.randbelow(encryption.curve.field.n)
    public_key = private_key * encryption.curve.g
    encrypted_message_text = encryption.encrypt_ECC(b_content, public_key)
    encrypted_message = {
        'ciphertext': binascii.hexlify(encrypted_message_text[0]),
        'nonce': binascii.hexlify(encrypted_message_text[1]),
        'authTag': binascii.hexlify(encrypted_message_text[2]),
        'ciphertextPubKey': hex(encrypted_message_text[3].x) + hex(encrypted_message_text[3].y % 2)[2:]
    }
    decrypted_text = encryption.decrypt_ECC(encrypted_message_text, private_key).decode('utf-8')

    print('Text:')
    print(content, end='\n\n')
    print('Encrypted message:')
    print(encrypted_message, end='\n\n')
    print('Decrypted text:')
    print(decrypted_text, end='\n\n')


if __name__ == '__main__':
    main()
