from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.move_food()

    def move_food(self):
        self.speed("fastest")
        self.goto(randint(-260, 260), randint(-260, 260))

