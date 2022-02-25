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

def get_coords(current_pos, length, width):
    return ((current_pos[0] * 11) + 5, (current_pos[1] * 11) + 5, (current_pos[0] * 11) + 5 + length, (current_pos[1] * 11) + 5 + width)

def get_circle(current_pos):
    return ((current_pos[0] * 11) + 2, (current_pos[1] * 11) + 2, (current_pos[0] * 11) + 6, (current_pos[1] * 11) + 6)

def get_line1(current_pos):
    return ((current_pos[0] * 11) + 2, (current_pos[1] * 11) + 2, (current_pos[0] * 11) + 6, (current_pos[1] * 11) + 6)

def get_line2(current_pos):
    return ((current_pos[0] * 11) + 6, (current_pos[1] * 11) + 2, (current_pos[0] * 11) + 2, (current_pos[1] * 11) + 6)

def get_end_line(x1,y1,x2,y2):
    return ((x1 * 11) + 6, (y1 * 11) + 6, (x2 * 11) + 6, (y2 * 11) + 6)

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
    refresh_image(board_state)
    return True

def game_over(board_state):
    for i in range(3):
        for j in range(3):
            try:
                if board_state[i][j] == board_state[i+1][j+1] == board_state[i+2][j+2] != "":
                    image = refresh_image(board_state)
                    draw = ImageDraw.Draw(image)
                    draw.line(get_end_line(i,j,i+2,j+2), fill="red")
                    matrix.SetImage(image)
                    return True
            except:
                1
            try:
                if board_state[i][j] == board_state[i+1][j-1] == board_state[i+2][j-2] != "":
                    image = refresh_image(board_state)
                    draw = ImageDraw.Draw(image)
                    draw.line(get_end_line(i,j,i+2,j-2), fill="red")
                    matrix.SetImage(image)
                    return True
            except:
                1
            try:
                if board_state[i][j] == board_state[i][j+1] == board_state[i][j+2] != "":
                    image = refresh_image(board_state)
                    draw = ImageDraw.Draw(image)
                    draw.line(get_end_line(i,j,i,j+2), fill="red")
                    matrix.SetImage(image)
                    return True
            except:
                1
            try:
                if board_state[i][j] == board_state[i+1][j] == board_state[i+2][j] != "":
                    image = refresh_image(board_state)
                    draw = ImageDraw.Draw(image)
                    draw.line(get_end_line(i,j,i+2,j), fill="red")
                    matrix.SetImage(image)
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
    end = False
    while True:
        k = readkey()
        if k == "q":
            break
        if not end:
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
                    end = True
                    print("game over")
                    print("press any key to restart")
        else:
            if k:
                image = get_board()
                base_image = get_board()
                board_state = [["","",""],["","",""],["","",""]]
                matrix.SetImage(image)
                current_pos = (0,0)
                pointer_init(current_pos)
                marker = "X"
                end = False
                
except KeyboardInterrupt:
    sys.exit(0)

    