import turtle
from turtle import Turtle
import time

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.no_of_segments = []
        self.create_snake()
        self.head = self.no_of_segments[0]

    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_segment(pos)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.no_of_segments.append(new_segment)

    def reset_snake(self):
        for seg in self.no_of_segments:
            seg.goto(1000, 1000)
        self.no_of_segments.clear()
        self.create_snake()
        self.head = self.no_of_segments[0]

    def extend_segment(self):
        self.add_segment(self.no_of_segments[-1].position())

    def move(self):
        for seg_no in range(len(self.no_of_segments) - 1, 0, -1):  # len used because we do not know how many segments
            # will be there
            new_x = self.no_of_segments[seg_no - 1].xcor()
            new_y = self.no_of_segments[
                seg_no - 1].ycor()  # getting the x and y coordinates of the second last snake segments
            self.no_of_segments[seg_no].goto(new_x, new_y)  # using the coordinates of second last segment to move
            # last segment and repeating it till we reach the first segment
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
