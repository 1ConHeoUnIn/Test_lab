
  int nut1=2;
  int nut2=3;
  void setup()
  {
    pinMode(nut1, INPUT_PULLUP); // chưa nhấn thì =1
    

    Serial.begin(9600);
  }

  void loop()
  {
    int trangthai1=digitalRead(nut1);
    
    Serial.println(trangthai1);
    
  delay(100);

    
  }