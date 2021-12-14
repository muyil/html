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

//Read humidity as %
int h = dht.readHumidity();

//Read temperature as Celsius (the default)
int t = dht.readTemperature();

//We put „code“ as a new variable, which should return the UID as a number. 
//Instead of int we are using long now to make use of bigger numbers.
long code=0;

//Seriel.print() will send data into Rasperry Pi and we can read it later
//with arduino.readLine()
//print humidity
Serial.print(h);

//for splitting
Serial.print("!t");

//print temperature
Serial.print(t);

//for new line
Serial.print("\n"); 

  //code-value from rasperry pi's 'arduino.write(byte(---->>>>>'1'<<<<<---, 'utf-8'))' to tell the arduino which servo
  //should be called.
  i= Serial.readString().toInt();
  if(i==1){
    //bring door servo to standart position.
    servoMotor1.write(0);
    delay(500);

    //Door-Servo
    //go to open state in +5 steps to make it more natural.
    for(int i = 0; i<100; i+=5){
        servoMotor1.write(i);
        delay(150);
    }

    delay(1000);

    //Door-Servo
    //go to close state in -5 steps to make it more natural.
    for(int i = 100; i>0; i-=5){
        servoMotor1.write(i);
        delay(150);
    }
  }

  if(i==2){
    //bring window servo to standart position.
    servoMotor2.write(0);
    delay(500);

    //Window-Servo
    //go to open state in +5 steps to make it more natural.
    for(int i = 0; i<100; i+=5){
        servoMotor2.write(i);
        delay(150);
    }
  }

 if(i==3){
    //Window-Servo
    //go to close state in -5 steps to make it more natural.
    for(int i = 100; i>0; i-=5){
        servoMotor2.write(i);
        delay(150);
    }
}

//Check if card is readed
if ( ! mfrc522.PICC_IsNewCardPresent())
{
return;
}

//Check if card is hold into the sensor
if ( ! mfrc522.PICC_ReadCardSerial())
{
return;
}

//If both check above are true than read the card code.
for (byte i = 0; i < mfrc522.uid.size; i++)
{
  //Now all 4 blocks are been read and in every run the code is multiplied with 10. (In normal cases you would use 1000 but that would make the number to big.)
  code=((code+mfrc522.uid.uidByte[i])*10);
}
Serial.println(code);
}
