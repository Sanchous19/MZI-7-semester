import os
import sys

from gost.gost3410 import CURVES
from gost.gost3410 import public_key
from gost.gost3410 import sign_3411
from gost.utils import bytes2long


def read_file(file):
    with open(file, 'r') as f:
        return f.read()


def main():
    content = read_file(sys.argv[1])
    b_content = content.encode('utf-8')

    private_key1 = bytes2long(os.urandom(32))
    private_key2 = bytes2long(os.urandom(32))
    curve = CURVES["id-GostR3410-2001-TestParamSet"]
    public_key1 = public_key(curve, private_key1)
    public_key2 = public_key(curve, private_key2)
    signature1 = sign_3411(curve, private_key1, public_key2, b_content)
    signature2 = sign_3411(curve, private_key2, public_key1, b_content)
    assert signature1 == signature2

    print(content, end='\n\n')
    print(signature1)


if __name__ == '__main__':
    main()
