#include <Arduino.h>
#include <ESP32Servo.h>
Servo myservo;

int servoPin =18;

void setup() {
myservo.attach(servoPin);
Serial.begin(115200);
}

void loop() {
  if(Serial.available()){
    int angle=Serial.parseInt();
    myservo.write(angle);
  }
  Serial.print("Angle:");
  Serial.println(myservo.read());
  delay(20);
}



