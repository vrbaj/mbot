#include <Arduino.h>
#include <Wire.h>
#include <SoftwareSerial.h>

#include <MeMCore.h>

MeDCMotor motor_9(9);
MeDCMotor motor_10(10);

void move(int direction, int speed)
{
  int leftSpeed = 0;
  int rightSpeed = 0;
  if (direction == 1) {
    leftSpeed = speed;
    rightSpeed = speed;
  } else if (direction == 2) {
    leftSpeed = -speed;
    rightSpeed = -speed;
  } else if (direction == 3) {
    leftSpeed = -speed;
    rightSpeed = speed;
  } else if (direction == 4) {
    leftSpeed = speed;
    rightSpeed = -speed;
  }
  motor_9.run((9) == M1 ? -(leftSpeed) : (leftSpeed));
  motor_10.run((10) == M1 ? -(rightSpeed) : (rightSpeed));
}

double angle_rad = PI / 180.0;
double angle_deg = 180.0 / PI;
String msg;
MeSerial se;
MeRGBLed rgbled_7(7, 7 == 7 ? 2 : 4);



void setup() {
  Serial.begin(115200);

}

void loop() {
while (se.available()) {
    delay(3);  //delay to allow buffer to fill 
    if (se.available() >0) {
      char c = se.read();  //gets one byte from serial buffer
      msg += c; //makes the string readString
    } 
  }

  if (msg.length() >0) {
      se.println(msg); //see what was received
      if(msg[0]=='1'){
      rgbled_7.setColor(0, 255, 255, 255);
      rgbled_7.show();  
      }
      if(msg[0]=='2'){
      rgbled_7.setColor(0,50, 0,0);
      rgbled_7.show();  
      }  
      Serial.println("..was the message");


    msg="";
  } 

//  if (se.read() > 0) {
//    msg = se.read();
//    se.println(msg);
//    rgbled_7.setColor(0, 0, 50, 0);
//    rgbled_7.show();    
//    _delay(1);
//    if (((msg[1]) == ('1'))) {
//      rgbled_7.setColor(0, 255, 255, 255);
//      rgbled_7.show();
//      msg = 'a';
//      se.println(msg);
//      _delay(5);
//    } else {
//      rgbled_7.setColor(0, 150, 0, 100);
//
//      rgbled_7.show();
//      msg = 'b';
//      se.println(msg);
//      _delay(5);
//    }
//  } else {
//    rgbled_7.setColor(0, 0, 0, 0);
//
//    rgbled_7.show();
//  }


  _loop();
}

void _delay(float seconds) {
  long endTime = millis() + seconds * 1000;
  while (millis() < endTime)_loop();
}

void _loop() {

}

