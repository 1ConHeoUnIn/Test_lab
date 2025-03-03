#include<IRremote.h>
const int chanRemote=10;
IRrecv irrecv(chanRemote); // tạo đối tượng IRrecv
decode_results results; // hiển thị kết quả

void setup() {
  Serial.begin(9600);
  irrecv.enableIRIn(); //cho phép nhận kết quả


}

void loop() {
  if(irrecv.decode(&results))
  {
    Serial.println(results.value, HEX);
    delay(200);
    irrecv.resume(); // nhận giá trị tiếp theo
  }

}
//FF02FD up
//FF9867 down
//FFE01F left
//FF906F right
