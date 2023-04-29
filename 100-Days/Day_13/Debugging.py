# step 1: Describe the problem

def my_function():
    for i in range(1, 20):
        if i == 20:
            print("you got it")

my_function()
# find and fix the error
year = int(input("what's your year of birth: "))
if 1980 < year < 1994:
    print("you are a millenial")
elif year > 1994:
    print("you are a Gen Z.")


# reproduce the bug
from random import randint
dice_ings = ["1*", "2*", "3*", "4*", "5*", "6*"]
dice_num = randint(1,6)
print(dice_ings[dice_num])





# fix the Error
# age = input("how old are you? ")
# if age > 18:
#     print(f"you can drive at age {age}")



# def mutuate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)
#
#
# mutuate([1,2,3,4,5])