class Car:
    runs = True

# initializer function
# the __ indicates it's special
    def __init__(self, name):
        print("new car!")
        self.name = name

    def start(self):
        if self.runs:
            print(f"{self.name} car is started")
        else:
            print(f"{self.name} car is broken :(!")
