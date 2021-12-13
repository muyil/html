from flask import Flask
import json
import datetime
import serial
import time
import re
import threading
import databaseFun
import pymysql
app = Flask(__name__)

connection = pymysql.connect(host="localhost", port=3306, user="root", passwd="Samy0110", database="WillenDafoeDb")
cursor = connection.cursor()

def get_temperature():
    cursor.execute("SELECT * FROM Temperatures")
    row_headers=[x[0] for x in cursor.description]
    result = cursor.fetchall()
    json_data=[]
    for result1 in result:
        json_data.append(dict(zip(row_headers,result1)))
    return json.dumps(json_data, indent=4, sort_keys=True, default=str)


@app.route("/getTemperature")
def hello():
    return get_temperature()

app.run(host='0.0.0.0', port=8090)

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

#####Processing Data

def main_function():

    while True:
        formatting_full_data()
#keycard = databaseFun.get_keycard(CODE)
#tkeycode = threading.Thread(target=formatting_keycode, args=([CODE]))
        global ISOPENED

#if keycard:
    #tkeycode.start()
    #tkeycode.join()

        if HUM > MAX_HUM and not ISOPENED:
            formatting_humidity(HUM)
            open_window(HUM)
            ISOPENED = True

        if HUM < MAX_HUM - 10 and ISOPENED:
            ISOPENED = False
            arduino.write(bytes('3', 'utf-8'))




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



def formatting_temperature(temp):
    if temp > MAX_TEMP:
        databaseFun.add_temperature(temp, 'Bitte Heizung runter regeln!')
    elif temp < MIN_TEMP:
        databaseFun.add_temperature(temp, 'Bitte Heizung hoch regeln!')

def formatting_humidity(hum):
    if hum > MAX_HUM:
        databaseFun.add_humidity(hum, 'Bitte lüften!')

def formatting_keycode(code):
    keycard = databaseFun.get_keycard(code)

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


### Initial
main_function()


### Threads
#t1 = threading.Thread(target=formatting_full_data, args=())
#t2 = threading.Thread(target=formatting_humidity, args=())
#t3 = threading.Thread(target=formatting_keycode, args=())
#twindow = threading.Thread(target=open_window, args=([HUM]))

#databaseFun.get_keycard(763100)
#databaseFun.get_user(1)

#t1.start()
#twindow.start()
#t2.start()
#t3.start()
#t1.join()
#twindow.join()
#t2.join()
#t3.join()
