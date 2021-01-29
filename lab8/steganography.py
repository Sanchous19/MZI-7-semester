from PIL import Image

BITMASK = 1
MAXCHANGE = 1
MAXLENGTH = 32
BYTELENGTH = 8


def tobits(s):
    result = ''
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result += bits
    return ''.join(result)


def frombits(bits):
    chars = []
    for b in range(len(bits) // 8):
        byte = bits[b * 8:(b + 1) * 8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)


def alignedbin32(val):
    binary = bin(val)[2:]

    if len(binary) < 32:
        binary = "0" * (32 - len(binary)) + binary

    return binary


def insert_into_byte(byte, bit):
    return ((byte >> 1) << 1) | bit


def insert_into_pixel(r, g, b, val):
    if len(val) == 1:
        val += "00"
    elif len(val) == 2:
        val += "0"

    x, y, z = tuple(map(int, val))

    r = insert_into_byte(r, x)
    g = insert_into_byte(g, y)
    b = insert_into_byte(b, z)

    return r, g, b


def get_from_pixel(r, g, b):
    return str(r & BITMASK) + str(g & BITMASK) + str(b & BITMASK)


def get_length(parsed_pixels):
    bin_length = parsed_pixels[:MAXLENGTH]
    return int(bin_length, base=2)


def get_bytes(parsed_pixels):
    batch_count = len(parsed_pixels) // BYTELENGTH
    batches = [parsed_pixels[i: i + BYTELENGTH] for i in range(batch_count)]

    byte_array = list(map(lambda x: int(x, base=2), batches))
    return list(bytearray(byte_array))


def hide(message, image_name, result_image_name):
    img = Image.open(image_name)
    pixels = img.load()

    message_bits = tobits(message)
    length_bits = alignedbin32(len(message_bits))
    all_bits = length_bits + message_bits

    pixelcount = 0
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if pixelcount >= len(all_bits):
                break

            r, g, b = pixels[i, j]

            val = all_bits[pixelcount: pixelcount + MAXCHANGE * 3]

            pixels[i, j] = insert_into_pixel(r, g, b, val)

            pixelcount += MAXCHANGE * 3

    newimg = Image.new(img.mode, img.size)
    newpixels = newimg.load()

    for i in range(newimg.size[0]):
        for j in range(newimg.size[1]):
            newpixels[i, j] = pixels[i, j]

    newimg.save(result_image_name)


def show(image_name):
    img = Image.open(image_name)
    pixels = img.load()

    hidden_bits = ""
    hidden_bits_length = 10 ** 8
    hidden_bits_length_initialized = False

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if (not hidden_bits_length_initialized
                    and len(hidden_bits) > MAXLENGTH):
                hidden_bits_length = get_length(hidden_bits)
                hidden_bits = hidden_bits[MAXLENGTH:]
                hidden_bits_length_initialized = True

            if len(hidden_bits) > hidden_bits_length:
                break

            r, g, b = pixels[i, j]
            hidden_bits += get_from_pixel(r, g, b)

    hidden_bits = hidden_bits[:hidden_bits_length]
    hidden_text = frombits(hidden_bits)

    return hidden_text
