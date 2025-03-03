int led_xanh=8; //cho chân số 8 kết nối với led xanh
int led_do=9; //cho chân số 9 kết nối với led đỏ
void setup() {
  pinMode (led_xanh, OUTPUT); //led là đầu ra
  pinMode (led_do, OUTPUT);
}

void loop() {
  digitalWrite(led_xanh, HIGH);// led ở trạng thái on
  digitalWrite(led_do, LOW);
  delay(100); //delay 0.1s
  digitalWrite(led_xanh, LOW); //led ở trạng thái off
  digitalWrite(led_do, HIGH);
  delay(100); //delay 0.1s

}
