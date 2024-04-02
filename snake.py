from turtle import *
import os
os.chdir("D:\python\\100dayscode\snake game")
screen = Screen()
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
screen.register_shape('up.gif')
screen.register_shape('down.gif')
screen.register_shape('left.gif')
screen.register_shape('right.gif')
screen.register_shape('horbody.gif')
screen.register_shape('upbody.gif')

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position1 in STARTING_POSITIONS:
            self.add_segment(position1)
        self.segments[0].shape('right.gif')

    def move(self):
        for piece_num in range(len(self.segments) - 1, 0, -1):
            self.segments[piece_num].goto(self.segments[piece_num - 1].pos())
        self.segments[0].forward(20)

    def add_segment(self, position):
        turtle = Turtle()
        turtle.shape("horbody.gif")
        turtle.penup()
        turtle.setpos(position)
        self.segments.append(turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
            self.segments[0].shape('up.gif')
            for segment in self.segments[1:]:
                segment.shape("upbody.gif")

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
            self.segments[0].shape('down.gif')
            for segment in self.segments[1:]:
                segment.shape("upbody.gif")

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
            self.segments[0].shape('left.gif')
            for segment in self.segments[1:]:
                segment.shape("horbody.gif")

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
            self.segments[0].shape('right.gif')
            for segment in self.segments[1:]:
                segment.shape("horbody.gif")
