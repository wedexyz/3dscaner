
#include <Stepper.h>
#include <Servo.h>
#include <math.h>
#define STEPS 100

Servo m; 
Stepper myStepper(STEPS, 8, 9, 10, 11);
const int stepsPerRevolution = 200;
int pos = 0;  
int t = 3;
int e=  2;
int n;  

void setup() {
  Serial.begin(9600);
  pinMode(t, OUTPUT);  //trigger pin
  pinMode(e, INPUT);  
  m.attach(13);;
  myStepper.setSpeed(30);
 
}
int distance(){
  
  long duration, cm;
  digitalWrite(t, LOW);
  delayMicroseconds(2);
  digitalWrite(t, HIGH);
  delayMicroseconds(5);
  digitalWrite(t, LOW);
  duration = pulseIn(e, HIGH);
  cm = duration/ 29 / 2;
  return cm; 
}
void scan(){
  int i;
  for(i=70;i<=120;i+=1){
    m.write(i);
    delay(25);      
    float d= distance();
    if (d<30){
      Serial.print(n);
      Serial.print(",");
      Serial.print(d*cos((i-90)*3.14/180));
      Serial.print(",");
      Serial.println(d*sin((i-90)*3.14/180));
      }
  }
  
  for(i=120;i>=70;i-=1){
    m.write(i);
    delay(25);
    }

}


  
void stp(){
  
  //Serial.println("clockwise");
  myStepper.step(stepsPerRevolution);
  //delay(500);
  }

void loop() {
  int i;

  //Serial.println("Start");
  for(i=0;i<20;i+=1){ // scan 20 times, every revolution is 18° i.e. 20x18° = 360°
    n=i;
   //Serial.println(i);
    scan();       //scan top to bottom
    stp();
    delay(50);  //repeat    
    
  }
 
 //Serial.println("End");
 delay(50);

 
  
}
