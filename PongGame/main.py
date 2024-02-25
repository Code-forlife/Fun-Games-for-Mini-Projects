from turtle import Screen
from paddle import Paddle
from scoreboard import ScoreBoard
from Ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.listen()
screen.title("Pong Game")
screen.tracer(0)

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
score = ScoreBoard()


screen.onkey(key="Up", fun=paddle1.move_up)
screen.onkey(key="Down", fun=paddle1.move_down)
screen.onkey(key="w", fun=paddle2.move_up)
screen.onkey(key="s", fun=paddle2.move_down)
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with main paddle
    if (ball.distance(paddle1) < 50 and ball.xcor() > 320) or (ball.distance(paddle2) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    elif ball.xcor() > 400:
        score.l_point()
        ball.reset()

    if ball.xcor() < -400:
        score.r_point()
        ball.reset()

screen.exitonclick()
