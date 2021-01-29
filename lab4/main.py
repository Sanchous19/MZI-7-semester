import sys

import el_gamal


def read_file(file):
    with open(file, 'r') as f:
        return f.read()


def main():
    content = read_file(sys.argv[1])

    private_key = el_gamal.generate_private_key(8)
    session_key = private_key.get_session_key()

    print('Text:')
    print(content, end='\n\n')
    encrypted_text = session_key.encrypt(content)
    print('Encrypted text:')
    print(encrypted_text, end='\n\n')
    decrypted_text = private_key.decrypt(encrypted_text)
    print('Decrypted text:')
    print(decrypted_text, end='\n\n')


if __name__ == '__main__':
    main()
