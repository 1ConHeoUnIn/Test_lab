
int nut=2;
int led=3;
void setup()
{
  pinMode(nut, INPUT);
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  int trangthai=digitalRead(nut);
  Serial.println(trangthai);//In ra trạng thái hiện tại
 
  Serial.println(trangthai);
  
}