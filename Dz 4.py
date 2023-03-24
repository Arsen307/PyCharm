class Parent1:
    def __init__(self):
        self.parent1_attribute = "Attribute Parent1"

class Parent2:
    def __init__(self):
        self.parent2_attribute = "Attribute Parent2"

class Child(Parent1, Parent2):
    def __init__(self):
        super().__init__()
        self.child_attribute = "Child attribute"
        self.parent2_attribute = "Attribute Parent2"

start = Child()
print(start.parent1_attribute)
print(start.parent2_attribute)
print(start.child_attribute)