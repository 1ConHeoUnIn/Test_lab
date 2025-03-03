// C++ code
//
int led=3;
int nut =2;
int trangthailed=0;
void setup()
{
  pinMode(led, OUTPUT);
  pinMode(nut, INPUT);
  Serial.begin(9600);
  digitalWrite(led,LOW); // ban đầu thì led tắt
}

void loop()
{
 int trangthainut=digitalRead(nut);
 
 
 int ledsang=digitalRead(led);
  Serial.println(trangthainut); // kiểm tra nút bấm

 
  if(trangthainut==1 && ledsang==trangthailed)// khi bấm nút thì đảo trạng thái
  {
  digitalWrite(led, !trangthailed);
     delay(500);
    trangthailed= !trangthailed;
   
  }
   
}