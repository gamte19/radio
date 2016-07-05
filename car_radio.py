from radio import Radio
import random


class CarRadio(Radio):
    def __init__(self, position, *args):
        self.position = position
        super().__init__(*args)

    def navigate(self, destination):
        print("your position is " + self.position)
        print(str(random.randint(0, 10)) + " km far from " + destination)
