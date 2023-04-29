# with open("weather_data.csv", "r") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
#
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data['temp']))
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(data["temp"].mean())
# print(data["temp"].max())
# tuesday = data[data.day == "Tuesday"]
# print(tuesday)
# tuesday_temp = int(tuesday.temp)

# CREATE A DATAFRAME FROM SCRATCH
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
#
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
#
# file = pandas.read_csv("new_data.csv")
# print(file)


# import pandas
# data = pandas.read_csv("4.1 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_squirrels_count)
# print(cinnamon_squirrels_count)
# print(black_squirrels_count)
#
# data_dict = {
#     "fur_color": ["Gray", "Cinnamon", "Black"],
#     "count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
# }
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")


# U.S GAME PART 1
import turtle
from turtle import Turtle, Screen
import pandas

tur_tle = Turtle()


screen = Screen()
screen.title("U.S Game")
image = "blank_states_img.gif"
screen.addshape(image)
tur_tle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct",
                                    prompt="what's another state? ").title()
    if answer_state == "Exit":
        # missing_states = []
        # for state in all_states:
        #     if state not in missing_states:
        #         missing_states.append(state)
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("remaining_states.csv")

        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

pandas.DataFrame()