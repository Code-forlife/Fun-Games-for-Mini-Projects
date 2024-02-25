from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_distance = 10
        self.y_distance = 10
        self.move_speed = 0.1
    def move(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce_y()
        new_xcor = self.xcor() + self.x_distance
        new_ycor = self.ycor() + self.y_distance
        self.goto(new_xcor, new_ycor)

    def bounce_y(self):
        self.y_distance *= -1

    def bounce_x(self):
        self.x_distance *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.home()
        self.move_speed = 0.1
        self.bounce_x()

