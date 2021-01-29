import md5


def main():
    content = (
        "I have to go to the university now but I will come back soon.",
        "We go jogging every Sunday.",
        "George hasn't finished his work yet.",
    )

    for string in content:
        print(string, '->', md5.MD5.hash(string))


if __name__ == '__main__':
    main()
