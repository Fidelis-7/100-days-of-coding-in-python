from turtle import Turtle, Screen

tim = Turtle()


def move_forward():
    tim.forward(10)


screen = Screen()
screen.listen()
screen.onkey(fun=move_forward, key="space")
screen.exitonclick()

