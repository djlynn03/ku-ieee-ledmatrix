#!/usr/bin/env python
from mimetypes import init
import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw

# if len(sys.argv) < 2:
#     sys.exit("Require an image argument")
6
# else:
#     image_file = sys.argv[1]

options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options = options)

# def cycle_image(index):
#     image_file = image_names[index]
#     image = Image.open(image_file)
    
#     image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
    
#     enhancer = ImageEnhance.Contrast(image)
#     image = enhancer.enhance(3)
    
#     matrix.SetImage(image.convert('RGB'))

def initialize():   # initializes tic tac toe grid
    image = Image.new("RGB", (32,32))
    draw = ImageDraw.Draw(image)
    
    draw.line((10,0,10,31), fill=(100,100,100))
    draw.line((21,0,21,31), fill=(100,100,100))

    draw.line((0,10,31,10), fill=(100,100,100))
    draw.line((0,21,31,21), fill=(100,100,100))

    matrix.Clear()
    matrix.SetImage(image)

# Configuration for the matrix

try:
    print("Press CTRL-C to stop.")
    while True:
        initialize()
        # movement = input()
        # if movement == 'a':
            
except KeyboardInterrupt:
    sys.exit(0)

    