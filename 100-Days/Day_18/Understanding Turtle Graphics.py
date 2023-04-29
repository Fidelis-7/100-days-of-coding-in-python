
from turtle import Turtle, Screen

# creating turtle class
our_turtle = Turtle()
# to change the shape of the turtle
# our_turtle.shape("arrow")
# to change the color of our turtle
our_turtle.color("blue")
# to move our turtle in order to make a square
for turtle in range(4):
    our_turtle.forward(100)
    our_turtle.right(90)

# for _ in range(15):
#     our_turtle.forward(10)
#     our_turtle.penup()
#     our_turtle.forward(10)
#     our_turtle.pendown()


screen = Screen()
screen.exitonclick()


