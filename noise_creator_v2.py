import numpy as np
from PIL import Image
from statistics import mode

ran = .05
def apply_constant_noise(bits):
    bits ^= np.random.random(bits.shape) < ran

    return bits

def triple_up(arr):
    return np.repeat(arr, 3)


def triple_up_decode(arr):

    def tally(list):
        return mode(list)

    #chunk every 3 bits and consolidate them
    de_tripled = np.zeros(int(arr.size/3), dtype = arr.dtype)
    for i in range (0, arr.size, 3):
        de_tripled[int(i/3)] = tally([arr[i],arr[i+1], arr[i+2]])

    return np.packbits(de_tripled)


def load_image_data():
    in_image = 'gradient.png'

    img = Image.open(in_image)
    mode = img.mode
    size = img.size

    in_bytes = np.array(img.getdata(), dtype=np.uint8)
    return (in_bytes,mode,size)

def print_image():
    in_image = 'gradient.png'

    img = Image.open(in_image)
    img.show()

def no_ecc():

    (data,mode,size) = load_image_data()
    bits = np.unpackbits(data)
    new_data = np.packbits(apply_constant_noise(bits))
    Image.frombytes(mode,size, new_data).show()

def ecc():
    (data,mode,size) = load_image_data()
    bits = triple_up(np.unpackbits(data))
    noised_transmission = apply_constant_noise(bits)
    new_data = triple_up_decode(noised_transmission)
    Image.frombytes(mode,size, new_data).show()

if __name__ == "__main__":
    print_image()
    no_ecc()
    ecc()
