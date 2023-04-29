age: int

age = "twelve"



def police_check(age:int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False

    return can_drive

if police_check(34):
    print("pay a fine")
else:
    print("move along")