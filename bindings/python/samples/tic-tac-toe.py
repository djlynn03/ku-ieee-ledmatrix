#!/usr/bin/env python
import time
import sys

from numpy import place
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

def get_circle(current_pos):
    return ((current_pos[0] * 10) + 2, (current_pos[1] * 10) + 2, (current_pos[0] * 10) + 6, (current_pos[1] * 10) + 6)

def get_line1(current_pos):
    return ((current_pos[0] * 10) + 2, (current_pos[1] * 10) + 2, (current_pos[0] * 10) + 6, (current_pos[1] * 10) + 6)

def get_line2(current_pos):
    return ((current_pos[0] * 10) + 6, (current_pos[1] * 10) + 2, (current_pos[0] * 10) + 2, (current_pos[1] * 10) + 6)

def get_board():   # initializes tic tac toe grid
    image = Image.new("RGB", (32,32))
    draw = ImageDraw.Draw(image)
    
    draw.line((10,0,10,31), fill=(100,100,100))
    draw.line((21,0,21,31), fill=(100,100,100))

    draw.line((0,10,31,10), fill=(100,100,100))
    draw.line((0,21,31,21), fill=(100,100,100))

    return image

def pointer_up(current_pos, image):
    if current_pos[1] == 0:
        return current_pos
    current_pos = (current_pos[0], current_pos[1] - 1)
    
    # image = get_board()
    draw = ImageDraw.Draw(image)
    
    draw.rectangle(get_coords(current_pos, 2,2), fill=(255,0,0))
    matrix.SetImage(image)
    return current_pos

def pointer_left(current_pos, image):
    if current_pos[0] == 0:
        return current_pos
    current_pos = (current_pos[0] - 1, current_pos[1])
    
    draw = ImageDraw.Draw(image)
    
    draw.rectangle(get_coords(current_pos, 2,2), fill=(255,0,0))
    matrix.SetImage(image)
    return current_pos

    
def pointer_right(current_pos, image):
    if current_pos[0] == 2:
        return current_pos
    current_pos = (current_pos[0] + 1, current_pos[1])

    
    # image = get_board()
    draw = ImageDraw.Draw(image)
    
    draw.rectangle(get_coords(current_pos, 2,2), fill=(255,0,0))
    matrix.SetImage(image)
    return current_pos

    
def pointer_down(current_pos, image):
    if current_pos[1] == 2:
        return current_pos
    current_pos = (current_pos[0], current_pos[1] + 1)
    # else:
    #     return 
    
    # image = get_board()
    draw = ImageDraw.Draw(image)
    
    draw.rectangle(get_coords(current_pos, 2,2), fill=(255,0,0))
    matrix.SetImage(image)
    return current_pos
# Configuration for the matrix

def pointer_init(current_pos):
    image = get_board()
    draw = ImageDraw.Draw(image)
    
    draw.rectangle(get_coords(current_pos, 2,2), fill=(255,0,0))
    matrix.SetImage(image)

def place_marker(current_pos, marker, base_image):
    draw = ImageDraw.Draw(base_image)
    
    if marker == "O":
        draw.ellipse(get_circle(current_pos), outline="gray")
        marker = "X"
        
    elif marker == "X":
        draw.line(get_line1(current_pos), fill="gray")
        draw.line(get_line2(current_pos), fill="gray")
        marker = "O"
        
    matrix.SetImage(base_image)
    
    return marker, base_image

try:
    print("type 'q' to quit")
    image = get_board()
    base_image = get_board()
    matrix.SetImage(image)
    current_pos = (0,0)
    pointer_init(current_pos)
    marker = "X"
    while True:
        k = readkey()
        if k == "q":
            break
        print(k, k == "q", k ==" ")
        
        if k == "w":
            current_pos = pointer_up(current_pos, image)
        elif k == 's':
            current_pos = pointer_down(current_pos, image)
        elif k == 'a':
            current_pos = pointer_left(current_pos, image)
        elif k == 'd':
            current_pos = pointer_right(current_pos, image)
        
        elif k == " ":
            marker,image = place_marker(current_pos, marker, base_image)
        
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

    