import turtle as t
import random

turtle = t.Turtle()
turtle.speed("fastest")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
directions = [0, 90, 180, 270]  # east, north, west, south directions
turtle.pensize(10)
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour


for _ in range(200):
    turtle.color(random_color())
    turtle.forward(30)
    turtle.setheading(random.choice(directions))
