def fullname():
    """input first and last name and prints them."""
    return f"my name is {firstname} {lastname}"


firstname = input("enter firstname: ")
lastname = input("enter lastname: ")
print(fullname())