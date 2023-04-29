with open("/Users/Fidelis/Desktop/invited_names.txt") as file:
    contents = file.read()
    print(contents)


with open("invited_names.txt", mode="a") as file:
    file.write("\nI am 20 years old. this is a new text")
