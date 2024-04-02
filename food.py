from turtle import *
import random
import os
os.chdir("D:\python\\100dayscode\snake game")
screen = Screen()
screen.register_shape('apple.gif')


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("apple.gif")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_spot = random.randint(-280, 280)
        self.goto(random_spot, random_spot)
