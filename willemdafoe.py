import serial
import time
import pymysql
import re
import threading

# database initialization
#####################
connection = pymysql.connect(host="localhost", port=3306, user="root", passwd="Samy0110", database="WillenDafoeDb")
cursor = connection.cursor()

###################################
###################################

########Makro
MAX_TEMP = 19 #23
MIN_TEMP = 19

####Temperatur
def add_temperature(value, description):
    query = "INSERT INTO Temperatures (Temperature, Description) VALUES ({},'{}');".format(value,description)
    cursor.execute(query)
    connection.commit()
    print("New meassured Temperature and is added to db")

def get_temperature():
    cursor.execute("SELECT * FROM Temperatures")
    result = cursor.fetchall();
    print("Entries:\n" + result)

####Humidity
def add_humidity(value, description):
    query = "INSERT INTO Humidities (Humidity, Description) VALUES ({},'{}');".format(value,description)
    cursor.execute(query)
    print("New meassured Humidity is added to db")

def get_humidity():
    cursor.execute("SELECT * FROM Humidities")
    result = cursor.fetchall();
    print("Entries:\n" + result)

def formatting_full_data():
    data = str(arduino.readline())
    pieces = data.split("!t")

    temp = int(re.search(r'\d+', pieces[1]).group())
    humidity = int(re.search(r'\d+', pieces[0]).group())

    print("Temperature: " + str(temp))
    print("Humidity: " + str(humidity))

def formatting_temperature():
    data = str(arduino.readline())
    pieces = data.split("!t")

    temp = int(re.search(r'\d+', pieces[1]).group())

    return temp

def printHi():
    while True:
        time.sleep(5)
        print("hi jari")


def printMoe():
    while True:
        time.sleep(1)
        print("moe lol")


t1 = threading.Thread(target=printHi, args=())
t2 = threading.Thread(target=printMoe, args=())

###Board
arduino = serial.Serial('/dev/ttyACM0')
arduino.baudrate=9600

####Pins


i = 0

while True:

#    t1.start()
#    t2.start()

#    t1.join()
#    t2.join()

    formatting_full_data()
    if formatting_temperature() > MAX_TEMP:
        add_temperature(formatting_temperature(), 'heizung ausschalten')
    elif formatting_temperature() < MIN_TEMP:
        add_temperature(formatting_temperature(), 'heizung anschalten')
