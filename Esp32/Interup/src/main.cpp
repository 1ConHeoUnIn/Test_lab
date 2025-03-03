#include <Arduino.h>

#define button1 27  // First button pin
#define button2 32  // Second button pin
#define led1 26     // First LED pin
#define led2 14     // Second LED pin

// Interrupt handler for button 1
void IRAM_ATTR detectPush1() {
  digitalWrite(led1, HIGH);
}

// Interrupt handler for button 2
void IRAM_ATTR detectPush2() {
  digitalWrite(led2, HIGH);
}

void setup() {
  Serial.begin(115200);

  pinMode(button1, INPUT_PULLUP);
  pinMode(button2, INPUT_PULLUP);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);

  // Attach interrupt for button 1 (RISING edge)
  attachInterrupt(digitalPinToInterrupt(button1), detectPush1, RISING);

  // Attach interrupt for button 2 (FALLING edge)
  attachInterrupt(digitalPinToInterrupt(button2), detectPush2, FALLING);
}

void loop() {
  // Your loop code here (can be empty or contain other logic)
}
