#include <Wire.h>
#include <QMC5883LCompass.h>
#include <Adafruit_MPU6050.h>
#include <PID_v1.h>

// Motor driver pins (replace with your actual pins)
#define MOTOR_LEFT_FWD 16
#define MOTOR_LEFT_BWD 17
#define MOTOR_RIGHT_FWD 18
#define MOTOR_RIGHT_BWD 19

// PID parameters (tune these!)
double Kp = 2.0;
double Ki = 0.05;
double Kd = 0.1;

// PID variables
double setpoint, input, output;
PID myPID(&input, &output, &setpoint, Kp, Ki, Kd, DIRECT);

// Sensor objects
QMC5883LCompass compass;
Adafruit_MPU6050 mpu;

float targetHeading = 0.0; // Initial target heading
float currentHeading = 0.0;
float gyroAngle = 0.0;
unsigned long previousMillis = 0;
float dt = 0.01; // Time step (adjust as needed)

void setup() {
  Serial.begin(115200);
  Wire.begin();

  // Initialize sensors
  if (compass.init()) {
    Serial.println("QMC5883L initialized successfully");
  } else {
    Serial.println("QMC5883L initialization failed");
    while (1); // Halt if initialization fails
  }
  // Calibrate the compass (replace with your values)
  compass.setCalibration(-1000, 1000, -1000, 1000);

  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1);
  }
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);

  // Initialize motor pins
  pinMode(MOTOR_LEFT_FWD, OUTPUT);
  pinMode(MOTOR_LEFT_BWD, OUTPUT);
  pinMode(MOTOR_RIGHT_FWD, OUTPUT);
  pinMode(MOTOR_RIGHT_BWD, OUTPUT);

  // Initialize PID
  setpoint = 0; // Set the target heading (0 degrees initially)
  myPID.SetMode(AUTOMATIC);
  myPID.SetOutputLimits(-255, 255); // Adjust based on your motor driver
}

void loop() {
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= 10) { // Run every 10ms
    previousMillis = currentMillis;
    dt = (float)(currentMillis - previousMillis) / 1000.0;

    // Read sensors
    compass.read();
    float compassAngle = compass.getAzimuth();

    sensors_event_t a, g, temp;
    mpu.getEvent(&a, &g, &temp);
    float gyroRate = g.gyro.z;
    gyroAngle += gyroRate * dt;

    // Sensor fusion (complementary filter)
    currentHeading = (0.98 * gyroAngle) + (0.02 * compassAngle);

    // PID control
    input = currentHeading;
    myPID.Compute();

    // Motor control
    int baseSpeed = 150; // Adjust base speed
    int leftSpeed = baseSpeed;
    int rightSpeed = baseSpeed;

    if (output > 0) { // Turn right
      rightSpeed -= output;
    } else if (output < 0) { // Turn left
      leftSpeed += output;
    }

    // Constrain speeds
    leftSpeed = constrain(leftSpeed, 0, 255);
    rightSpeed = constrain(rightSpeed, 0, 255);

    // Set motor speeds (replace with your motor driver code)
    analogWrite(MOTOR_LEFT_FWD, leftSpeed);
    analogWrite(MOTOR_LEFT_BWD, 0);
    analogWrite(MOTOR_RIGHT_FWD, rightSpeed);
    analogWrite(MOTOR_RIGHT_BWD, 0);
  }
}
