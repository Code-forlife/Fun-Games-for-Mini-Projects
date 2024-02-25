from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        self.shape("square")
        # shapesize()
        self.penup()
        self.goto(location)
        self.shapesize(5, 1)
        self.color("white")

    def move_up(self):
        new_y = self.ycor() + 20
        new_x = self.xcor()
        self.goto(new_x, new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        new_x = self.xcor()
        self.goto(new_x, new_y)