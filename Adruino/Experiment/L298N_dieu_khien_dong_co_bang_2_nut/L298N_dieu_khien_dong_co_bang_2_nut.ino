

int inA=8;
  int inB=9;
  int nut_up=6;
  int nut_down=7;

void setup() {
  pinMode (inA, OUTPUT);
  pinMode (inB, OUTPUT);
  pinMode (nut_up, INPUT_PULLUP);
  pinMode (nut_down, INPUT_PULLUP);
Serial.begin(9600);

}

void loop() {
  int up_state=digitalRead(nut_up);

  int down_state=digitalRead(nut_down);
    Serial.println(up_state);
    Serial.println(down_state);

    if(up_state ==0 && down_state !=0)
    {
      go_up();
    }
    else if(up_state !=0 && down_state ==0)
    {
      go_down();
    }
    else 
    {
      stop();
    }

}

void go_up() {
    analogWrite(inA, 150);
    digitalWrite(inB, LOW);

}

void go_down() {
    digitalWrite(inA, LOW);
    analogWrite(inB, 150);
    
}

void stop() {
    digitalWrite(inA, LOW);
    digitalWrite(inB, LOW);
    
}
