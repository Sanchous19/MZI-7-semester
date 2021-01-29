import steganography


def main():
    text = (
        "I have to go to the university now but I will come back soon." +
        "We go jogging every Sunday." +
        "George hasn't finished his work yet."
    )
    input_image_name = 'input.png'
    hidden_image_name = 'hidden.png'

    steganography.hide(text, input_image_name, hidden_image_name)
    hidden_text = steganography.show(hidden_image_name)

    print('Text:')
    print(text)
    print()
    print('Hidden text:')
    print(hidden_text)


if __name__ == "__main__":
    main()
