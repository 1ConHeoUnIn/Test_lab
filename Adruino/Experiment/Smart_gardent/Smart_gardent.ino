int moisture, analog_sensor;
const int sensor_pin =A1; //chân Vp
const int relay = 12;
int dry_percent;
void setup() {
 Serial.begin(9600);
 pinMode(relay, OUTPUT);
 digitalWrite(relay, LOW);

}

void loop() {
  analog_sensor= analogRead(sensor_pin);
  dry_percent= map(analog_sensor,0,1023,0,100); //10bit
moisture = 100-dry_percent;
Serial.print("\f analog = " );
  Serial.println(analog_sensor);
  Serial.print("dry = " );
  Serial.println(dry_percent);
  Serial.print(" moisture = " );
  Serial.print(moisture);
  Serial.println("%");
  delay(300);

  if (moisture<20)
  {
    digitalWrite(relay, HIGH);
    Serial.println("bad");
  }
  else 
  {
    digitalWrite(relay,LOW);
    Serial.println("good");
  }
  delay(1000);
}