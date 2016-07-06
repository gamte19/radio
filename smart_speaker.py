from radio import Radio


class SmartSpeaker(Radio):
    def __init__(self, memory, *args):
        self.memory = memory
        super().__init__(*args)

    def memory_upgrade(self, upgrade):
        print("My old storage size is " + str(self.memory))
        self.memory = self.memory + upgrade
        print("My current storage size is " + str(self.memory))
