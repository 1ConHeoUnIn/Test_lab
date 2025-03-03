// C++ code
//
int up=4;
int left=2;
int right=5;
int motor1=6;
int motor2=7;
void setup()
{
  pinMode(up, INPUT_PULLUP);
  pinMode(left, INPUT_PULLUP);
  pinMode(right, INPUT_PULLUP);
  pinMode(motor1, OUTPUT);
  pinMode(motor2, OUTPUT);
  Serial.begin(9600);
  digitalWrite(motor1,LOW);
   digitalWrite(motor2, LOW);
}

void loop()
{
  int upStatus=digitalRead(up);
  int leftStatus=digitalRead(left);
  int rightStatus=digitalRead(right);
  Serial.println(upStatus);
  if(upStatus==0)
  {
    digitalWrite(motor1, HIGH);
    digitalWrite(motor2, HIGH);
  }
  else if(leftStatus==0)
  {
    digitalWrite(motor1, HIGH);
    digitalWrite(motor2, LOW);
  }
  else if(rightStatus==0)
  {
    digitalWrite(motor1, LOW);
    digitalWrite(motor2, HIGH);
  }
  else
  {
    
    digitalWrite(motor1, LOW);
    digitalWrite(motor2, LOW);
    }

}