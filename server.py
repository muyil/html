from flask import Flask
import pymysql
import json
import datetime
import serial
app = Flask(__name__)

###Board
arduino = serial.Serial('/dev/ttyACM0')
arduino.baudrate=9600

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

def get_humidity():
    cursor.execute("SELECT * FROM Humidities")
    row_headers=[x[0] for x in cursor.description]
    result = cursor.fetchall()
    json_data=[]
    for result1 in result:
        json_data.append(dict(zip(row_headers, result1)))
    return json.dumps(json_data, indent=4, sort_keys=True, default=str)

@app.route("/temperature")
def temperature():
    return get_temperature()

@app.route("/humidity")
def humidity():
    return get_humidity()

@app.route("/door")
def test():
    print("App wurde erkannt")
    arduino.write(bytes('1', 'utf-8'))
    time.sleep(1)
    arduino.write(bytes('0', 'utf-8'))
    return"test"

app.run(host='0.0.0.0', port=8090)
