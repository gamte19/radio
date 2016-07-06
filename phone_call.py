from smart_speaker import SmartSpeaker


class PhoneCall(SmartSpeaker):
    def __init__(self, phone_number, *args):
        super().__init__(*args)
        self.phone_number = phone_number

    def make_phone_call(self, give_phone_number):
        print("My number is " + self.phone_number + " and I'm calling " + give_phone_number)
