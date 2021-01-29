import sys

import des


def check_des_double(text):
    print('----------------- Double DES -----------------', end='\n\n')

    print('Text:')
    print(text, end='\n\n')

    key1 = des.get_random_key()
    key2 = des.get_random_key()
    print(f'Keys: key1 = {key1}, key2 = {key2}', end='\n\n')

    encrypted_text = des.encrypt_double(text.encode('utf-8'), key1, key2)
    print('Encrypted text:')
    print(encrypted_text, end='\n\n')

    decrypted_text = des.decrypt_double(encrypted_text, key1, key2).decode('utf-8')
    print('Decrypted text:')
    print(decrypted_text, end='\n\n')

    print('----------------------------------------------', end='\n\n')


def check_des_triple(text):
    print('----------------- Triple DES -----------------', end='\n\n')

    print('Text:')
    print(text, end='\n\n')

    key1 = des.get_random_key()
    key2 = des.get_random_key()
    key3 = des.get_random_key()
    print(f'Keys: key1 = {key1}, key2 = {key2}, key3 = {key3}', end='\n\n')

    encrypted_text = des.encrypt_triple(text.encode('utf-8'), key1, key2, key3)
    print('Encrypted text:')
    print(encrypted_text, end='\n\n')

    decrypted_text = des.decrypt_triple(encrypted_text, key1, key2, key3).decode('utf-8')
    print('Decrypted text:')
    print(decrypted_text, end='\n\n')

    print('----------------------------------------------', end='\n\n')


def main():
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        content = f.read()

    for i in range(8 - len(content) % 8):
        content += ' '
    check_des_double(content)
    check_des_triple(content)


if __name__ == '__main__':
    main()
