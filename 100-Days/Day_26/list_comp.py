names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = []
for name in names:
    if len(name) < 5:
        short_names.append(name)
print(short_names)


# List comprehension for squared numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number**2 for number in numbers]
print(squared_numbers)

# List comprehension for even numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [even for even in numbers if even % 2 == 0]
print(result)

with open("file1.txt") as file1:
    content1 = file1.readlines()

with open("file2.txt") as file2:
    contents2 = file2.readlines()

results = [int(number) for number in content1 if number in contents2]
print(results)



