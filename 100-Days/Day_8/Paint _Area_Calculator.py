Height = int(input("enter the height of the wall: "))
Width = int(input("enter the width of the wall: "))
coverage = 5


def paint_calc(height, width, cover):
    area = Height * width
    number_of_cans = round(area / coverage)
    print(f"you will need {number_of_cans} cans of paint")


paint_calc(height=Height, width=Width, cover=coverage)


