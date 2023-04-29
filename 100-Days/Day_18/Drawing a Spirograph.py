from turtle import Turtle, Screen
import random

tortoise = Turtle()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tortoise.forward(100)
        tortoise.right(angle)


for shape_sides in range(3, 11):
    tortoise.color(random.choice(colors))
    draw_shape(shape_sides)


screen = Screen()
screen.exitonclick()