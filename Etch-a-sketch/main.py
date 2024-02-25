import turtle
tim = turtle.Turtle()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def move_left():
    # tim.setheading(tim.heading()-10)
    tim.left(10)


def move_right():
    # tim.setheading(tim.heading()+10)
    tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


my_screen = turtle.Screen()
my_screen.listen()
my_screen.onkey(key="w", fun=move_forward)
my_screen.onkey(key="s", fun=move_backward)
my_screen.onkey(key="a", fun=move_left)
my_screen.onkey(key="d", fun=move_right)
my_screen.onkey(key="c", fun=clear)
my_screen.exitonclick()

