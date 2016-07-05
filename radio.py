class Radio():
    CONNECTION = ["wifi", "bluetooh", "cable"]

    def __init__(self, brand, size, colour, item_of_speaker, music, connection):
        self.brand = brand
        self.size = size
        self.colour = colour
        self.item_of_speaker = item_of_speaker
        self.music = music
        if connection not in self.CONNECTION:
            raise ValueError("I'm not a valid type of connection")
        else:
            self.connection = connection

    def play_song(self):
        print("I'm playing " + self.music)

    def say_connection_type(self):
        if self.connection is "cable":
            print("I'm an old radio because my type of connection is: " + self.connection)
        elif self.connection is "bluetooh":
            print("You can use me any time if you have another gadget which has bluetooh connection")
        elif self.connection is "wifi":
            print("You can use me if you have internet connection")

    def introduce_myself(self):
        print("My brand is " + self.brand)
        print("My size is " + self.size + " cm")
        print("My colour is " + self.colour)
        print("I have " + self.item_of_speaker + " speaker(s)")
        print("I can plya " + self.music)
        print("My connection type is " + self.connection)
