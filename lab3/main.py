import sys

import rsa


def read_file(file):
    with open(file, 'r') as f:
        return f.read()


def main():
    content = read_file(sys.argv[1])

    public_key, private_key = rsa.make_key_pair(8)
    print('Text:')
    print(content, end='\n\n')
    encrypted_text = public_key.encrypt(content)
    print('Encrypted text:')
    print(encrypted_text, end='\n\n')
    decrypted_text = private_key.decrypt(encrypted_text)
    print('Decrypted text:')
    print(decrypted_text, end='\n\n')


if __name__ == '__main__':
    main()
