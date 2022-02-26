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
        # self.pos = [0,0]
        self.positions = [[0,0]]
        # self.segment_positions = [self.pos]
        self.length = 1
        self.food = Food()
        
    def move(self, direction):
        self.positions.append([self.positons[len(self.positions)-1][0] + direction[0], self.positons[len(self.positions)-1][1] + direction[1]])
        if not self.check_eat:
            self.positions.remove(self.positions[0])
        else:
            self.length += 1
        
    # def grow(self):
    #     self.length += 1
        
    def check_death(self):
        if self.pos[0] == 32 or self.pos[0] == -1 or self.pos[1] == 32 or self.pos[1] == -1 or len(self.positions) != len(set(self.positions)):
            return True
        return False
    
    def check_eat(self):
        return self.positions[len(self.positions) - 1] == self.food.pos
        # if self.pos == self.food.pos:
        #     self.length += 1
        #     del self.food
        #     self.food = Food()
        
    def draw_image(self):
        image = Image.new("RGB", (32,32))           # create a new imagemd
        draw = ImageDraw.Draw(image)                # create a drawing object
        draw.point(self.food.pos, fill=(255,0,0))   # red dot for food
        
        for segment in self.positions:
            draw.point(segment, fill=(0,255,0))     # green line for snake body
        matrix.SetImage(image)
        


try:
    print("type 'q' to quit, 'c' to clear")
    end = False
    snake = Snake()
    snake.draw_image()
    dir = [0,0]
    while True:
        snake.draw_image
        k = readkey()
        if k == "q":
            break
        if not end:
            if k == "w":
                dir = [0,-1]
            elif k == 's':
                dir = [0,1]
            elif k == 'a':
                dir = [-1,0]
            elif k == 'd':
                dir = [1,0]
                
            snake.move(dir)
            
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
            