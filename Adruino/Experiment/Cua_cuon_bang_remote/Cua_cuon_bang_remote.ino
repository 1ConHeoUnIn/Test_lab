#include<IRremote.h>
const int chanRemote=10;
IRrecv irrecv(chanRemote); // tạo đối tượng IRrecv
decode_results results; // hiển thị kết quả

int ctht1=3;
int ctht2=4;
int inA=8;
int inB=9;


void setup() {
  pinMode(ctht1, INPUT);
  pinMode(ctht2, INPUT);
  pinMode(inA, OUTPUT);
  pinMode(inB, OUTPUT);
  Serial.begin(9600);
  irrecv.enableIRIn();

  
}

void loop() {
  int ctht1_state = digitalRead(ctht1);
  int ctht2_state = digitalRead(ctht2);

 

  Serial.println(ctht1_state);
  Serial.println(ctht2_state);

  if(irrecv.decode(&results))
   {
   
    if(results.value ==0xFF02FD ) // remote điều khiển 
  {
    while(ctht1_state!=1) //khi nào chạm công tắc hành trình thì dừng
    {
     
 
      go_up();
      ctht1_state= digitalRead(ctht1);
      
    }
      stop();
    

  }
  else if(results.value ==0xFF9867 ){
    while(ctht2_state !=1)
    {
  

      go_down();
      ctht2_state= digitalRead(ctht2);
     
    }
    stop();
  
  
  }
  else {
    stop();
    
  }
    irrecv.resume();
   }
  
}

void go_up(){
  digitalWrite(inA, HIGH);
  digitalWrite(inB, LOW);

}

void go_down(){
  digitalWrite(inA, LOW);
  digitalWrite(inB, HIGH);

}

void stop(){
  digitalWrite(inA, LOW);
  digitalWrite(inB, LOW);
}

