import random
print("*** Welcome to the PyPassword Generator ***")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
symbols = ["!","@","#","$","%","^", "&", "*", "(", ")", "+", "-", "/", "|"]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
user_choice_1 = int(input("how many letters would you like in your password? "))
user_choice_2 = int(input("how many numbers would you like in your password? "))
user_choice_3 = int(input("how many symbols would you like in your password? "))
password_list = []
for char in range(1, user_choice_1 + 1):
    password_list.append(random.choice(letters))

for char in range(1, user_choice_2 + 1):
    password_list.append(str(random.choice(numbers)))

for char in range(1, user_choice_3 + 1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"your password is {password}")