from phone_call import PhoneCall
from car_radio import CarRadio


class SmartCarRadio(PhoneCall, CarRadio):

    def __init__(self, data_limit, *args):
        super().__init__(*args)
        self.data_limit = data_limit

    def normalize_phone_number(self):
        self.phone_number = self.phone_number.replace(" ", "").replace("-", "")
        return self.phone_number

    def make_normalized_number_calling(self, number):
        normalized_call = self.normalize_phone_number()
        print("Im calling " + number + " and my number is " + self.phone_number)

    def browse_the_web(self):
        print("Facebok")
        print("your data limit " + str(self.data_limit) + "MB")
        self.data_limit -= 1
