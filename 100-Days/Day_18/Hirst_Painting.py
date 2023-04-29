import turtle
from turtle import Screen

import random

tim = turtle.Turtle()
turtle.colormode(255)
color_list = [(254, 254, 23), (138, 73, 48), (55, 54, 39), (230, 143, 97), (93, 12, 67), (191, 108, 74)]
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()