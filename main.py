import time
from turtle import *
from Player import *
from Puck import *
from Scoreboard import *

screen = Screen()
screen.title("Pong The Game")
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)

left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)

screen.update()
pen = Chalk()
ball = Puck()
scoreboard = Scoreboard()
pen.draw_field()
screen.update()

screen.listen()
screen.onkey(right_paddle.go_up, "Up",)
screen.onkey(right_paddle.go_down, "Down",)
screen.onkey(left_paddle.go_up, "w",)
screen.onkey(left_paddle.go_down, "s",)


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Ball goes out of bound RIGHT SIDE
    if ball.xcor() > 385:
        ball.reset_position()
        scoreboard.r_point()

    # Ball goes out of bound LEFT SIDE
    if ball.xcor() < -385:
        ball.reset_position()
        scoreboard.l_point()


screen.exitonclick()