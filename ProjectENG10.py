import board
from adafruit_hcsr04 import HCSR04
from time import sleep

sonar = HCSR04(trigger_pin = board.TX, echo_pin = board.A6)
danger_dist = 120 #Lower than this is at a dangerous distance.

#Higher than this means the object has closed in on the device by a dangerous device.
danger_closing_dist = 50
danger_count = 1

#Offset of the array
offset = 1
sonar_array = [[],[],[],[],[],[],[],[],[],[]] #array of 10 empty arrays

def checkDanger(full_array):
    final_dist = full_array[9]
    closing_dist = full_array[0] - full_array[9]
    if((final_dist < danger_dist) & (closing_dist > danger_closing_dist)):
        print("full_array:", full_array)
        return True
    return False

while True:
    for index in range(offset):
        sonar_array[index].append(sonar.distance)
        print(sonar.distance)
        if(len(sonar_array[index]) == 10):
            if(checkDanger(sonar_array[index])):
                print("DANGER", danger_count)
                danger_count = danger_count + 1
            sonar_array[index].clear()
        sleep(0.1)

    #Will stop increasing offset at 5, which is when the offset will affect all arrays already.
    if(offset < 10):
        offset = offset + 1

