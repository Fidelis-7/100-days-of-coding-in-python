try:
    file = open("Day_30/a_file.txt")
    a_dict = {"key":"value"}
    print(a_dict["key"])

except FileNotFoundError:
    with open("Day_30/a_file.txt", mode="w") as file:
        file.write("Something")

except KeyError as error_message:
    print(f"{error_message} key not found")

else:
    content = file.read()
    print(content)

finally:
    raise TypeError("check the types")     # raising an error












# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Height is too high")

# BMI = weight / (height**2)
# print(BMI)

# fruits = ["Apple", "Pear", "Orange"]
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit Pie")

#     else:
#         print(fruit + " pie")
    
# make_pie(3)


facebooks_posts = [
    {'Likes':21, "comments":2},
    {'Likes':21, "comments":2, 'shares':1},
    {'Likes':33, "comments":8, "shares":3},
    {"shares":3, "comments":2},
    {"shares":3, "comments":1},
    {'Likes':19, "comments":3}
    
    ]

total_likes = 0
for post in facebooks_posts:
    try:
        total_likes += post['Likes']
    except KeyError:
        total_likes += 0 
    else:
        pass
print(total_likes)