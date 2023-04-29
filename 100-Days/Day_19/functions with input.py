def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    return n1 / n2


def calculator(n1, n2, func):
    return func(n1, n2)


result = calculator(4, 56, add)
print(result)
