import turtle as t
from turtle import Screen
import random
turtle = t.Turtle()
t.colormode(255)
turtle.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour


def draw_spirograph(size_of_gap):
    for _ in range(int(size_of_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + 10)


draw_spirograph(100)

screen = Screen()
screen.exitonclick()
