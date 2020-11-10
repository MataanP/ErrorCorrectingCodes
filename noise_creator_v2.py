import numpy as np
import random as rand
from PIL import Image

def randomize_bits(ran):
    rand.seed(4)

    img = Image.open("gradient.png")
    img.show()
    mode = img.mode
    size = img.size
    data = img.tobytes()

    #test = np.array(img.tobytes(),dtype=np.uint8)
    #Image.frombytes(mode,size, data).show()
    in_image = 'gradient.png'
    out_image = 'out_gradient.png'

    #in_bytes = np.fromfile(in_image, np.uint8)
    bits = np.unpackbits(data)

    for i, bit in enumerate(bits):
        if rand.random() < ran:
            bits[i] ^= bits[i]

    
    out_bytes = np.packbits(bits)
    #out_bytes.tofile(out_image)
    Image.frombytes(mode,size, out_bytes).show()
if __name__ == "__main__":
    randomize_bits(1)