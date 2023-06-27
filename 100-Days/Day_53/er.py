class Parent():
    def __init__(self, height, color, surname):
        self.height = height
        self.color = color
        self.surname = surname

    def family(self):
        print(f"we are the {self.surname} family")
        print(f"we are {self.color}")
        print(f"the average height in the family is {self.height}")


class FirstChild(Parent):
    def __init__(self, height, color, surname, name, siblings):
        super().__init__(height, color, surname)
        self.name = name
        self.sibling = siblings

    def child_name(self):
        print(f"my name is {self.name} and I have {self.sibling} siblings")
        


parents = Parent(5.67, "black", "Abanum")
first_child = FirstChild(5.67, "black", "Abanum", "Fidelis", 3)
first_child.child_name()
first_child.family()

