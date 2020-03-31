#include <AFMotor.h>

// Create objects for our two motors.
AF_DCMotor motor1(1);
AF_DCMotor motor2(2);

void setup() 
{
  motor1.setSpeed(200); // Ranges from 0 to 255. Can set anywhere.
  motor1.run(RELEASE); // Removes power from the motor.
  motor2.setSpeed(200);
  motor2.run(RELEASE);
}

void loop() 
{
  uint8_t s;

  // Turn on motor
  motor1.run(FORWARD);
  motor2.run(FORWARD);
  
  // Accelerate from zero to maximum speed
  for (s=0; s<255; s++)
  {
    motor1.setSpeed(s);  
    motor2.setSpeed(s);
    delay(10); // 100th of a second delay.
  }
  
  // Decelerate from maximum speed to zero
  for (s=255; s>=0; s--) 
  {
    motor1.setSpeed(s); 
    motor2.setSpeed(s);   
    delay(10);
  }

  motor1.run(BACKWARD); // Rotates in the opposite direction.
  motor1.run(BACKWARD);
  
  // Accelerate from zero to maximum speed
  for (s=0; s<255; s++)
  {
    motor1.setSpeed(s);  
    motor2.setSpeed(s);
    delay(10); // 100th of a second delay.
  }
  
  // Decelerate from maximum speed to zero
  for (s=255; s>=0; s--) 
  {
    motor1.setSpeed(s); 
    motor2.setSpeed(s);   
    delay(10);
  }

  // Now turn off motors
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  delay(1000);
}
