#!/usr/bin/env python
import time
import sys
import os
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageEnhance

if len(sys.argv) < 2:
    sys.exit("Require an image argument")
else:
    image_file = sys.argv[1]
image = Image.open(image_file)
image = image.convert('RGB')
print(image.mode)
# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 5
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options = options)

# Make image fit our screen.
image.thumbnail((matrix.width, matrix.height))
enhance = ImageEnhance.Contrast(image)
image = enhance.enhance(3)
#save_dir = '/home/pi/Desktop/rpi-rgb-led-matrix/rpi-rgb-led-matrix/bindings/python/samples'
matrix.SetImage(image.convert('RGB'))
#image.save(os.path.join(save_dir, 'test.png'))
try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)
