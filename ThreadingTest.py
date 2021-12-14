import serial
import time
import re
import threading
import databaseFun

###Board
#This is the port in which the arduino is connected to the PI
arduino = serial.Serial('/dev/ttyACM0')

#Rate of how fast data is send
arduino.baudrate=9600


########Makro-Variables
MAX_TEMP = 25
MIN_TEMP = 19

MAX_HUM = 60
MIN_HUM = 25

TEMP = 0
HUM = 0
CODE = 0
ISOPENED = False


#####Functions
def main_function():

    while True:
        formatting_full_data()
        global ISOPENED

        #Check if HUM exceeded max threshold and window is closed
        if HUM > MAX_HUM and not ISOPENED:
            formatting_humidity(HUM)
            open_window(HUM)

            ISOPENED = True

        #Check if HUM is now under 10% of the max threshold and window is open
        if HUM < MAX_HUM - 10 and ISOPENED:
            ISOPENED = False

            print("Fenster wird wieder geschlossen.")

            #Tell the Arduino to close the window
            arduino.write(bytes('3', 'utf-8'))

def formatting_full_data():
    #Get return value from Arduino and format it to string
    data = str(arduino.readline())

    #Split string at '!t' and put the values as an array in pieces
    pieces = data.split("!t")

    #count of pieces varies because the arduino return one value if you use the door
    #and 2 values if he check temperature and humidity.
    #So if the count of pieces is 1 we want to use our door function
    if len(pieces) == 1:
        #global tag so the compiler knows we want to overwrite our makros
        global CODE

        #Decimal value of the keycard hold into the door sensor
        CODE = int(re.search(r'\d+', pieces[0]).group())

        #A card code is always bigger than 1 this right here is just a check
        #if the card was readed correctly
        if CODE > 1:
            print("Code: " + str(CODE))
            formatting_keycode(CODE)

    #when count of pieces is 2 we want to know about temperature and humidity
    elif len(pieces) == 2:
        global TEMP
        global HUM

        #clear the string from pieces array into a pure integer and
        #initilize global TEMP and global HUM with new values.
        TEMP = int(re.search(r'\d+', pieces[1]).group())
        HUM = int(re.search(r'\d+', pieces[0]).group())

        print("Temperature: " + str(TEMP))
        print("Humidity: " + str(HUM))

def formatting_temperature(temp):
    #when temp exceeds max treshhold then add a new entry into the database
    if temp > MAX_TEMP:
        databaseFun.add_temperature(temp, 'Heizung wird runter gedreht!')
    #when temp fallen below min treshhold then add a new entry into the database
    elif temp < MIN_TEMP:
        databaseFun.add_temperature(temp, 'Heizung wird hoch gedreht!')

def formatting_humidity(hum):
    #when hum exceeds max threshold then add a new entry to the database 
    if hum > MAX_HUM:
        databaseFun.add_humidity(hum, 'Lütftung wird geregelt!')

def formatting_keycode(code):
    #check if the code is registered in our database
    keycard = databaseFun.get_keycard(code)

    #when registered keycard must be true
    if keycard:
        print("Keycard wurde erkannt. Willkommen.")
        
        #tell the door-servo within the arduino to go to open door position.
        arduino.write(bytes('1', 'utf-8'))

        #freeze the code for 5 seconds
        time.sleep(5)

        #tell the door-servo within the arduino to go to close door position.
        arduino.write(bytes('0', 'utf-8'))
    elif not keycard:
        print("Keycard nicht erkannt")

def open_window():
    print('Fenster wird geöffnet.')

    #tell the window-servo within the arduino to go to open window position.
    arduino.write(bytes('2', 'utf-8'))

    time.sleep(5)

    #tell the window-servo within the arduino to go to close window position.
    arduino.write(bytes('0', 'utf-8'))


### Initial
main_function()