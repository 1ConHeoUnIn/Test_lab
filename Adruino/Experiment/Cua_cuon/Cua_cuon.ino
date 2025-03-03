

int inA=8;
  int inB=9;
  int nut_up=6;
  int nut_down=7;
  int ctht1=3;
  int ctht2=4;

void setup() {
  pinMode (inA, OUTPUT);
  pinMode (inB, OUTPUT);
  pinMode (nut_up, INPUT_PULLUP);
  pinMode (nut_down, INPUT_PULLUP);
  pinMode (ctht1, INPUT);
  pinMode (ctht2, INPUT);
  
Serial.begin(9600);

}

void loop() {
  int up_state=digitalRead(nut_up);
  int down_state=digitalRead(nut_down);
   
  int ctht1_state = digitalRead(ctht1);
  int ctht2_state = digitalRead(ctht2);
     Serial.println(ctht1_state);
     Serial.println(ctht2_state);
  


    if(up_state ==0 && down_state !=0 && ctht1_state ==0) //khi đụng thanh dẫn thì dừng lại
    {
      go_up();
    }
    else if(up_state !=0 && down_state ==0 && ctht2_state ==0)
    {
      go_down();
    }
    else 
    {
      stop();
    }

}

void go_up() {
    analogWrite(inA, 130);
    digitalWrite(inB, LOW);

}

void go_down() {
    digitalWrite(inA, LOW);
    digitalWrite(inB, HIGH);
    
}

void stop() {
    digitalWrite(inA, LOW);
    digitalWrite(inB, LOW);
    
}
