#!/usr/bin/env python
import time
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw
from readchar import readkey, key
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

# current_pos = (0, 0)

def get_coords(current_pos, length, width):
    return ((current_pos[0] * 10) + 5, (current_pos[1] * 10) + 5, (current_pos[0] * 10) + 5 + length, (current_pos[1] * 10) + 5 + width)

def get_board():   # initializes tic tac toe grid
    image = Image.new("RGB", (32,32))
    draw = ImageDraw.Draw(image)
    
    draw.line((10,0,10,31), fill=(100,100,100))
    draw.line((21,0,21,31), fill=(100,100,100))

    draw.line((0,10,31,10), fill=(100,100,100))
    draw.line((0,21,31,21), fill=(100,100,100))

    return image

def pointer_up(current_pos):
    if current_pos[1] != 0:
        current_pos = (current_pos[0], current_pos[1] - 1)
    else:
        return
    
    image = get_board()
    draw = ImageDraw.Draw(image)
    
    draw.rectangle(get_coords(current_pos, 2,2), fill=(255,0,0))
    matrix.SetImage(image)

def pointer_left(current_pos):
    if current_pos[0] != 0:
        current_pos = (current_pos[0] - 1, current_pos[1])
    else:
        return
    
    image = get_board()
    draw = ImageDraw.Draw(image)
    
    draw.rectangle(get_coords(current_pos, 2,2), fill=(255,0,0))
    matrix.SetImage(image)
    
def pointer_right(current_pos):
    if current_pos[0] != 2:
        current_pos = (current_pos[0] + 1, current_pos[1])
    else:
        return
    
    image = get_board()
    draw = ImageDraw.Draw(image)
    
    draw.rectangle(get_coords(current_pos, 2,2), fill=(255,0,0))
    matrix.SetImage(image)
    
def pointer_down(current_pos):
    if current_pos[1] != 2:
        current_pos = (current_pos[0], current_pos[1] + 1)
    else:
        return
    
    image = get_board()
    draw = ImageDraw.Draw(image)
    
    draw.rectangle(get_coords(current_pos, 2,2), fill=(255,0,0))
    matrix.SetImage(image)
# Configuration for the matrix

def pointer_init(current_pos):
    image = get_board()
    draw = ImageDraw.Draw(image)
    
    draw.rectangle(get_coords(current_pos, 2,2), fill=(255,0,0))
    matrix.SetImage(image)
    
try:
    print("type 'q' to quit")
    matrix.SetImage(get_board())
    current_pos = (0,0)
    pointer_init(current_pos)

    while True:
        k = readkey()
        if k == "q":
            break
        print(k, k == "q")
        
        if k == "w":
            pointer_up(current_pos)
        elif k == 's':
            pointer_down(current_pos)
        elif k == 'a':
            pointer_left(current_pos)
        elif k == 'd':
            pointer_right(current_pos)
        if k:
            print(current_pos)
        # elif key == 'a':
        #     sys.exit(0)
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

    