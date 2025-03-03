int ctht1=3;
int ctht2=4;
void setup() {
  pinMode (ctht1, INPUT);
  pinMode (ctht2, INPUT);
  Serial.begin(9600);

}

void loop() {
  int ht1_state = digitalRead(ctht1);
  int ht2_state = digitalRead(ctht2);
  Serial.println(ht1_state);
  Serial.println(ht2_state);
  delay(100);

}
