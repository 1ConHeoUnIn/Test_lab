#include <Arduino.h>

const int servoPin = 2;

uint32_t pulseToDuty(int microseconds); // Khai báo prototype

void setup() {
  ledcSetup(0, 50, 16);           // Tần số 50Hz, độ phân giải 16 bit
  ledcAttachPin(servoPin, 0);
}

void loop() {
  ledcWrite(0, pulseToDuty(500));   // Góc 0°
  delay(1000);
  ledcWrite(0, pulseToDuty(1500));  // Góc 90°
  delay(1000);
  ledcWrite(0, pulseToDuty(2400));  // Góc 180°
  delay(1000);
}

uint32_t pulseToDuty(int microseconds) {
  return (uint32_t)((microseconds * 65536L) / 20000L);
}
