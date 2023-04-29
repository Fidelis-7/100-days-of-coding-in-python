import turtle
from turtle import Turtle, Screen
import random
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
y_positions = [-60, -30, 0, 30, 60, 90]
all_turtles = []

is_race_on = False
for turtle_index in range(6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput("Turtle Race", "who will win? ")
print(user_input)
if user_input:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"you have won!. The {winning_color} turtle is the winner.")
            else:
                print(f"you lost. The {winning_color} turtle is the winner")

        rand_position = random.randint(0, 10)
        turtle.forward(rand_position)
screen.exitonclick()
