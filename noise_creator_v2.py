import numpy as np

def randomize_bits(ran):
    in_image = 'gradient.png'
    out_image = 'out_gradient.png'

    in_bytes = np.fromfile(in_image, np.uint8)
    bits = np.unpackbits(in_bytes)

    for bit in bits:
        bit ^= bit
    
    out_bytes = np.packbits(bits)
    out_bytes.tofile(out_image)

if __name__ == "__main__":
    randomize_bits(1)