#!/usr/bin/env python

import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw
import random
import time
import tkinter
import matplotlib
matplotlib.use("TkAgg")
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
        self.positions.append([self.positions[len(self.positions)-1][0] + direction[0], self.positions[len(self.positions)-1][1] + direction[1]])
        if not self.check_eat:
            self.positions.remove(self.positions[0])
        else:
            self.length += 1
        
    # def grow(self):
    #     self.length += 1
        
    def check_death(self):
        return self.positions[len(self.positions) - 1][0] < 0 or self.positions[len(self.positions) - 1][0] > 31 or self.positions[len(self.positions) - 1][1] < 0 or self.positions[len(self.positions) - 1][1] > 31
    
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
        

class App:
    def __init__(self):
        print("type 'q' to quit, 'c' to clear")
        self.end = False
        self.snake = Snake()
        self.snake.draw_image()
        self.dir = [0,0]
        self.root = tkinter.Tk()
        self.root.bind('<KeyPress>', self.change_dir)
        
        # self.listener = pynput.keyboard.Listener(on_press=self.change_dir)
        # self.listener.start()
        # self.listener.join()
        
        while True:
            self.snake.draw_image()

            self.snake.move(dir)

            if self.snake.check_death():
                self.end = True
                print("Game over!\nPress any key to restart.")
                
            time.sleep(0.1)
            
    def change_dir(self, key):
        if key == 'q':
            print("Exiting...")
            sys.exit(0)
        if key == "w":
            self.dir = [0,-1]
        elif key == 's':
            self.dir = [0,1]
        elif key == 'a':
            self.dir = [-1,0]
        elif key == 'd':
            self.dir = [1,0]
        print(key)
        
app = App()