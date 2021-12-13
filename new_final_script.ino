#include "DHT.h"
#include <SPI.h>
#include <MFRC522.h>
#include <Servo.h>
#define SS_PIN 10
#define RST_PIN 9
#define SERVO_SIGNAL_PIN1 8
#define SERVO_SIGNAL_PIN2 7
MFRC522 mfrc522(SS_PIN, RST_PIN);
#define DHTPIN 2 // what digital pin we're connected to
Servo servoMotor1;
Servo servoMotor2;

int i = 0; // command for open the door
// Uncomment whatever type you're using!

#define DHTTYPE DHT11 // DHT 11

//#define DHTTYPE DHT22 // DHT 22 (AM2302), AM2321

//#define DHTTYPE DHT21 // DHT 21 (AM2301)

// Initialize DHT sensor.

DHT dht(DHTPIN, DHTTYPE);

void setup() {

Serial.begin(9600);

dht.begin();
SPI.begin();
mfrc522.PCD_Init();
servoMotor2.attach(SERVO_SIGNAL_PIN1, 900, 1500);
servoMotor1.attach(SERVO_SIGNAL_PIN2, 900, 1500);
servoMotor1.write(0);
servoMotor2.write(0);
}

void loop() {

delay(2000);

// Reading temperature or humidity takes about 250 milliseconds!

int h = dht.readHumidity();

// Read temperature as Celsius (the default)

int t = dht.readTemperature();

long code=0; // Als neue Variable fügen wir „code“ hinzu, unter welcher später die UID als zusammenhängende Zahl ausgegeben wird. Statt int benutzen wir jetzt den Zahlenbereich „long“, weil sich dann eine größere Zahl speichern lässt.

Serial.print(h);

Serial.print("!t"); // for splitting

Serial.print(t);

Serial.print("\n"); // for new line


  i= Serial.readString().toInt();
  if(i==1){
    servoMotor1.write(0);
    delay(500);

    servoMotor1.write(0);
    delay(500);


    for(int i = 0; i<100; i+=5){
        servoMotor1.write(i);
        delay(150);
    }

    delay(1000);

    for(int i = 100; i>0; i-=5){
        servoMotor1.write(i);
        delay(150);
    }
  }

  if(i==2){
    servoMotor2.write(0);
    delay(500);

    servoMotor2.write(0);
    delay(500);


    for(int i = 0; i<100; i+=5){
        servoMotor2.write(i);
        delay(150);
    }
  }

 if(i==3){
    for(int i = 100; i>0; i-=5){
        servoMotor2.write(i);
        delay(150);
    }
}

if ( ! mfrc522.PICC_IsNewCardPresent())
{
return;
}

if ( ! mfrc522.PICC_ReadCardSerial())
{
return;
}

for (byte i = 0; i < mfrc522.uid.size; i++)
{
code=((code+mfrc522.uid.uidByte[i])*10); // Nun werden wie auch vorher die vier Blöcke ausgelesen und in jedem Durchlauf wird der Code mit dem Faktor 10 „gestreckt“. (Eigentlich müsste man hier den Wert 1000 verwenden, jedoch würde die Zahl dann zu groß werden.
}
Serial.println(code);
}
