#!/usr/bin/env python
from operator import ilshift
from signal import raise_signal
import time
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw
import readchar
# if len(sys.argv) < 2:
#     sys.exit("Require an image argument")
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

current_pos = (0, 0)

def get_coords(length, width):
    return ((current_pos[0] * 10) + 5, (current_pos[1] * 10) + 5, (current_pos[0] * 10) + 5 + length, (current_pos[1] * 10) + 5 + width)

def get_board():   # initializes tic tac toe grid
    image = Image.new("RGB", (32,32))
    draw = ImageDraw.Draw(image)
    
    draw.line((10,0,10,31), fill=(100,100,100))
    draw.line((21,0,21,31), fill=(100,100,100))

    draw.line((0,10,31,10), fill=(100,100,100))
    draw.line((0,21,31,21), fill=(100,100,100))

    return image

def pointer_up():
    if current_pos[1] != 0:
        current_pos = (current_pos[0], current_pos[1] - 1)
    else:
        return
    
    image = get_board()
    draw = ImageDraw.Draw(image)
    
    draw.rectangle(get_coords, fill=(255,0,0))
    matrix.SetImage(image)

def pointer_left():
    if current_pos[0] != 0:
        current_pos = (current_pos[0] - 1, current_pos[1])
    else:
        return
    
    image = get_board()
    draw = ImageDraw.Draw(image)
    
    draw.rectangle(get_coords, fill=(255,0,0))
    matrix.SetImage(image)
    input()
def pointer_right():
    if current_pos[0] != 2:
        current_pos = (current_pos[0] + 1, current_pos[1])
    else:
        return
    
    image = get_board()
    draw = ImageDraw.Draw(image)
    
    draw.rectangle(get_coords, fill=(255,0,0))
    matrix.SetImage(image)
    
def pointer_down():
    if current_pos[1] != 2:
        current_pos = (current_pos[0], current_pos[1] + 1)
    else:
        return
    
    image = get_board()
    draw = ImageDraw.Draw(image)
    
    draw.rectangle(get_coords, fill=(255,0,0))
    matrix.SetImage(image)
# Configuration for the matrix

try:
    print("Press CTRL-C to stop.")
    matrix.SetImage(get_board())
    while True:
        key = repr(readchar.readkey())
        if key == '\x1b[A':
            pointer_up()
        elif key == '\x1b[B':
            pointer_down(0)
        elif key == '\x1b[D':
            pointer_left(0)
        elif key == '\x1b[C':
            pointer_right(0)
        else:
            break
    sys.exit(0)
    # turtle.listen()
    # turtle.onkey(pointer_up, "Up")
    # turtle.onkey(pointer_left, "Left")
    # turtle.onkey(pointer_right, "Right")
    # turtle.onkey(pointer_down, "Down")

    # while True:
    #     movement = input()
    #     # turtle.
    #     if movement:
    #         print(movement)
    #     # if movement == 'a':
            
except KeyboardInterrupt:
    sys.exit(0)

    