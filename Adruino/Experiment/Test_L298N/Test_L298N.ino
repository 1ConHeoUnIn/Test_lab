
  int in1=9;
  int in2=10;

void setup() {
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);

}

void loop() {
tien();
delay (3000);
dung();
delay (1000);
lui();
delay (3000);


}

void tien() {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);

}
void lui() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);

}
void dung() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);

}
