# constructing objects and Accessing their Attributes and Methods
# import turtle
#
# tortoise = turtle.Turtle()
# turtle.Screen().exitonclick()
# print(tortoise)

# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.color("blue")
# timmy.shape("turtle")
# timmy.right(90)
# timmy.penup()
# timmy.forward(100)


# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name", ["pikachu", "Squirtle", "chermander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "c"
print(table)