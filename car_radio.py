from radio import Radio
import random


class CarRadio(Radio):

    CONNECTION = ["bluetooh", "cable"]

    def __init__(self, position, *args):
        self.position = position
        super().__init__(*args)

    def navigate(self, destination):
        print("your position is " + self.position)
        print("You are " + str(random.randint(0, 10)) + " km far from " + destination)
