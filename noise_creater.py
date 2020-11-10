from PIL import Image

def constant_noise_creator_binary(byte_data):
    x= 9

def get_bit(value, n):
    return ((value >> n & 1) != 0)

def set_bit(value, n):
    return value | (1 << n)

def clear_bit(value, n):
    return value & ~(1 << n)

if __name__ == '__main__':

    img = Image.open("gradient.png")
    img.show()
    mode = img.mode
    size = img.size
    data = img.tobytes()

    Image.frombytes(mode,size, data).show()
