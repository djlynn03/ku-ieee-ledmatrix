#!/usr/bin/env python
import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageEnhance

# if len(sys.argv) < 2:
#     sys.exit("Require an image argument")
# else:
#     image_file = sys.argv[1]

image_names = ['grass_block_side.png', 'diamond_ore.png']

def cycle_image(index):
    image_file = image_names[index]
    image = Image.open(image_file)
    
    image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
    
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(3)
    
    matrix.SetImage(image.convert('RGB'))
    

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options = options)

i = 0
try:
    print("Press CTRL-C to stop.")
    while True:
        
        cycle_image(i)
        i += 1
        if i == len(image_names):
            i = 0
        time.sleep(0.5)
        
except KeyboardInterrupt:
    sys.exit(0)

    