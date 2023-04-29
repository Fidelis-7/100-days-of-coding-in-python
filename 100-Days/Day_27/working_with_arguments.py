def add(*args):
    print(args[0])
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(6, 4, 2, 9, 1))

def calc(**kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
        # print(key)
        # print(value)
    print(kwargs["add"])

calc(add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
