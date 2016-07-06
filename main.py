from radio import Radio
from smart_speaker import SmartSpeaker
from car_radio import CarRadio
from phone_call import PhoneCall
from smart_car_radio import SmartCarRadio

radio = Radio("Sony", "20", "black", "2", "Rihanna", "wifi")
smart_speaker = SmartSpeaker(1000, "Sony", "20", "black", "2", "Rihanna", "wifi")
car_radio = CarRadio("Blaha", "Sony", "20", "black", "2", "Rihanna", "cable")   # wifi is not allowed in CarRadio class
phone_call = PhoneCall("06 12-34-56", 1000, "Sony", "20", "black", "2", "Rihanna", "bluetooh")
smart_car_radio = SmartCarRadio("06 12-34-56", 1000, "ujpest", "Sony", "20", "black", "2", "Rihanna", "cable")

print("Radio " + "#" * 20)
radio.play_song()
radio.say_connection_type()
radio.introduce_myself()
print()
print("SmartSpeaker " + "#"*13, '\n')
print("introduce_myself:")
smart_speaker.introduce_myself()
print()
print("say_connection_type:")
smart_speaker.say_connection_type()
print()
print("memory_upgrade:")
smart_speaker.memory_upgrade(1024)
smart_speaker.memory_upgrade(1024)
print()
print("CarRadio" + "#"*18, '\n')
print("navigate")
car_radio.navigate("oktogon")
print()
print("make phone call:")
phone_call.make_phone_call("0000000000")
print("My normalized number: \n" + smart_car_radio.normalize_phone_number())
smart_car_radio.make_normalized_number_calling("12345667")
smart_car_radio.navigate("Ibrany")
