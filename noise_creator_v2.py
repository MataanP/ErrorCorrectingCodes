import numpy as np
from PIL import Image

def randomize_bits(ran):
    np.random.seed(4)

    in_image = 'gradient.png'

    img = Image.open(in_image)
    img.show()
    mode = img.mode
    size = img.size
   
    in_bytes = np.array(img.getdata(), dtype=np.uint8)
    bits = np.unpackbits(in_bytes)

    bits ^= np.random.random(bits.shape) < ran
    
    out_bytes = np.packbits(bits)
    Image.frombytes(mode,size, out_bytes).show()

if __name__ == "__main__":
    randomize_bits(.1)