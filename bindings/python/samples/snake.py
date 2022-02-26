#!/usr/bin/env python

import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw
from readchar import readkey, key
import random
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



class Food:
    def __init__(self):
        self.pos = [random.randint(0,31), random.randint(0,31)]
        
class Snake:
    def __init__(self):
        self.pos = [0,0]
        # self.segment_positions = [self.pos]
        self.length = 1
        self.food = Food()
        
    def move(self, direction):
        self.pos[0] += direction[0]
        self.pos[1] += direction[1]
        return self.pos
        
    def grow(self):
        self.length += 1
        
    def check_death(self):
        if self.pos[0] == 32 or self.pos[0] == -1 or self.pos[1] == 32 or self.pos[1] == -1:
            # or self.pos in self.segment_positions
            return True
        return False
    
    def check_eat(self):
        if self.pos == self.food.pos:
            self.length += 1
            del self.food
            self.food = Food()
        
    def draw_image(self):
        image = Image.new("RGB", (32,32))           # create a new imagemd
        draw = ImageDraw.Draw(image)                # create a drawing object
        draw.point(self.food.pos, fill=(255,0,0))   # red dot for food
        
        draw.point(self.pos, fill=(0,255,0))        # green dot for snake head
        # for segment in self.segment_positions:
        #     draw.point(segment, fill=(0,255,0))     # green line for snake body
        
        matrix.SetImage(image)
        


try:
    print("type 'q' to quit, 'c' to clear")
    end = False
    snake = Snake()
    while True:
        k = readkey()
        if k == "q":
            break
        if not end:
            if k == "w":
                current_pos = snake.move([0,-1])
            elif k == 's':
                current_pos = snake.move([0,1])
            elif k == 'a':
                current_pos = snake.move([-1,0])
            elif k == 'd':
                current_pos = snake.move([1,0])
            if snake.check_death():
                end = True
                print("Game over!\nPress any key to restart.")
            snake.check_eat()
        else:
            if k:
                snake = Snake()
                end = False
except:
    sys.exit(0)
            