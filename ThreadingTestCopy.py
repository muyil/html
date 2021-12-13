import serial
import time
import re
import threading

###Board
arduino = serial.Serial('/dev/ttyACM0')
arduino.baudrate=9600



########Makro
MAX_TEMP = 25
MIN_TEMP = 19

MAX_HUM = 60
MIN_HUM = 25

COUNT = 0
TEMP = 0
HUM = 0
CODE = 0
ISOPENED = False





def formatting_full_data():
    data = str(arduino.readline())
    pieces = data.split("!t")

    global COUNT

    COUNT = len(pieces)

    if len(pieces) == 1:
        global CODE
        CODE = int(re.search(r'\d+', pieces[0]).group())

        if CODE > 1:
            print("Code: " + str(CODE))
            formatting_keycode(CODE)

    elif len(pieces) == 2:
        global TEMP
        global HUM
        TEMP = int(re.search(r'\d+', pieces[1]).group())
        HUM = int(re.search(r'\d+', pieces[0]).group())

        print("Temperature: " + str(TEMP))
        print("Humidity: " + str(HUM))

        #formatting_temperature(TEMP)
        #formatting_humidity(HUM)



    if keycard:
        print("Keycard wurde erkannt. Willkommen.")
        arduino.write(bytes('1', 'utf-8'))
        time.sleep(5)
        arduino.write(bytes('0', 'utf-8'))
    elif not keycard:
        print("Keycard nicht erkannt")

def open_window(hum):
    print('Window is opening.')
    arduino.write(bytes('2', 'utf-8'))
    time.sleep(5)
    arduino.write(bytes('0', 'utf-8'))

def openDoor():
    print("App wurde erkannt")
    arduino.write(bytes('1', 'utf-8'))
    time.sleep(5)
    arduino.write(bytes('0', 'utf-8'))


print("test")
time.sleep(5)
