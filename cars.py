# import importlib
# importlib.reload(cars)
class Car:
    runs = True
    number_of_wheels = 4

# initializer function
# the __ indicates it's special
    def __init__(self, name):
        print("new car!")
        self.name = name

    def __str__(self):
        return f"My car the {self.name} currently {self.runs}"

    def __repr__(self):
        return f"Car({self.name})"

    def start(self):
        if self.runs:
            print(f"{self.name} car is started")
        else:
            print(f"{self.name} car is broken :(!")

    @classmethod
    def get_number_of_wheels(cls):
        return cls.number_of_wheels
