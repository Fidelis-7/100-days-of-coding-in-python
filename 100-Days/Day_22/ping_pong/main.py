from turtle import Turtle as Paddle, Screen
from Paddle import Paddle
from Ball import Ball
import time
from Scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(key="Up", fun=right_paddle.go_up)
screen.onkey(key="Down", fun=right_paddle.go_down)
screen.onkey(key="w", fun=left_paddle.go_up)
screen.onkey(key="s", fun=left_paddle.go_down)


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

#     Detect collision by wall
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()

#   Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

#   Detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

#   Detect left ball misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()


screen.exitonclick()