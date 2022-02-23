#!/usr/bin/env python
from nis import cat
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
    return ((current_pos[0] * 11) + 5, (current_pos[1] * 11) + 5, (current_pos[0] * 11) + 5 + length, (current_pos[1] * 11) + 5 + width)

def get_circle(current_pos):
    return ((current_pos[0] * 11) + 2, (current_pos[1] * 11) + 2, (current_pos[0] * 11) + 6, (current_pos[1] * 11) + 6)

def get_line1(current_pos):
    return ((current_pos[0] * 11) + 2, (current_pos[1] * 11) + 2, (current_pos[0] * 11) + 6, (current_pos[1] * 11) + 6)

def get_line2(current_pos):
    return ((current_pos[0] * 11) + 6, (current_pos[1] * 11) + 2, (current_pos[0] * 11) + 2, (current_pos[1] * 11) + 6)

def get_board():   # initializes tic tac toe grid
    image = Image.new("RGB", (32,32))
    draw = ImageDraw.Draw(image)
    
    draw.line((10,0,10,31), fill=(100,100,100))
    draw.line((21,0,21,31), fill=(100,100,100))

    draw.line((0,10,31,10), fill=(100,100,100))
    draw.line((0,21,31,21), fill=(100,100,100))

    return image

def refresh_image(board_state):
    temp = get_board()
    draw = ImageDraw.Draw(temp)
    for i in range(3):
        for j in range(3):
            if board_state[i][j] == "O":
                    draw.ellipse(get_circle((i,j)), outline="gray")
                    
            elif board_state[i][j] == "X":
                draw.line(get_line1((i,j)), fill="gray")
                draw.line(get_line2((i,j)), fill="gray")

    matrix.SetImage(temp)
    
    return temp
    
def pointer_up(current_pos, board_state):
    if current_pos[1] == 0:
        return current_pos
    
    current_pos = (current_pos[0], current_pos[1] - 1)
    
    image = refresh_image(board_state)
    # image = get_board()
    draw = ImageDraw.Draw(image)
    
    draw.rectangle(get_coords(current_pos, 2,2), fill=(255,0,0))
    matrix.SetImage(image)
    return current_pos

def pointer_left(current_pos, board_state):
    if current_pos[0] == 0:
        return current_pos
    current_pos = (current_pos[0] - 1, current_pos[1])
    
    image = refresh_image(board_state)

    draw = ImageDraw.Draw(image)
    
    draw.rectangle(get_coords(current_pos, 2,2), fill=(255,0,0))
    matrix.SetImage(image)
    return current_pos

    
def pointer_right(current_pos, board_state):
    if current_pos[0] == 2:
        return current_pos
    current_pos = (current_pos[0] + 1, current_pos[1])
    
    image = refresh_image(board_state)
    draw = ImageDraw.Draw(image)
    
    draw.rectangle(get_coords(current_pos, 2,2), fill=(255,0,0))
    matrix.SetImage(image)
    return current_pos

    
def pointer_down(current_pos, board_state):
    if current_pos[1] == 2:
        return current_pos
    current_pos = (current_pos[0], current_pos[1] + 1)
    # else:
    #     return 
    
    image = refresh_image(board_state)
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



def place_marker(current_pos, marker, board_state):
    if board_state[current_pos[0]][current_pos[1]] != "":
        return False
    board_state[current_pos[0]][current_pos[1]] = marker
    print(board_state)
    refresh_image(board_state)
    return True
    # draw = ImageDraw.Draw(base_image)
      
    # matrix.SetImage(base_image)
    
    # return marker, base_image
def game_over(board_state):
    for i in range(3):
        for j in range(3):
            try:
                if board_state[i][j] == board_state[i+1][j+1] == board_state[i+2][j+2] != "":
                    image = refresh_image(board_state)
                    draw = ImageDraw.Draw(image)
                    draw.line(get_line1((i,j)), fill="red")
                    return True
            except:
                1
            try:
                if board_state[i][j] == board_state[i+1][j-1] == board_state[i+2][j-2] != "":
                    image = refresh_image(board_state)
                    draw = ImageDraw.Draw(image)
                    draw.line(get_line2((i,j)), fill="red")
                    return True
            except:
                1
            try:
                if board_state[i][j] == board_state[i][j+1] == board_state[i][j+2] != "":
                    image = refresh_image(board_state)
                    draw = ImageDraw.Draw(image)
                    draw.line(get_line1((i,j)), fill="red")
                    return True
            except:
                1
            try:
                if board_state[i][j] == board_state[i+1][j] == board_state[i+2][j] != "":
                    image = refresh_image(board_state)
                    draw = ImageDraw.Draw(image)
                    draw.line(get_line1((i,j)), fill="red")
                    return True
            except:
                1

try:
    print("type 'q' to quit, 'c' to clear")
    image = get_board()
    base_image = get_board()
    board_state = [["","",""],["","",""],["","",""]]
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
            current_pos = pointer_up(current_pos, board_state)
        elif k == 's':
            current_pos = pointer_down(current_pos, board_state)
        elif k == 'a':
            current_pos = pointer_left(current_pos, board_state)
        elif k == 'd':
            current_pos = pointer_right(current_pos, board_state)
        
        elif k == " ":
            if place_marker(current_pos, marker, board_state):
                print("marker placed")
                if marker == "X":
                    marker = "O"
                elif marker == "O":
                    marker = "X"
        elif k == "c":
            image = get_board()
            base_image = get_board()
            board_state = [["","",""],["","",""],["","",""]]
            matrix.SetImage(image)
            current_pos = (0,0)
            pointer_init(current_pos)
            marker = "X"
            
        if k:
            if game_over(board_state):
                print("game over")
                
            
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

    