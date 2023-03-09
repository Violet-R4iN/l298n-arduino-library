
#include "Arduino.h"
#include "movecore.h"
movecore::movecore (int ENP1, int ENP2, int ENA, int ENB, int ENP3, int ENP4){
      ctrlP1 = ENP1;
      ctrlP2 = ENP2;
      EN1 = ENA;
      EN2 = ENB;
      ctrlP3 = ENP3;
      ctrlP4 = ENP4;
    }

void movecore::pinSetup(){
  pinMode(ctrlP1, OUTPUT);
  pinMode(ctrlP2, OUTPUT);
  pinMode(ctrlP3, OUTPUT);
  pinMode(ctrlP4, OUTPUT);
  pinMode(EN1, OUTPUT);
  pinMode(EN2, OUTPUT);
}

void movecore::sequence01(int x)
{
    if (x ==1)
    {
      digitalWrite(ctrlP1, LOW);
      digitalWrite(ctrlP2, LOW);
      digitalWrite(ctrlP3, LOW);
      digitalWrite(ctrlP4, LOW);
      Serial.println("robot stop executed");
    }
    if (x == 2)
    {
      digitalWrite(ctrlP1, HIGH);
      digitalWrite(ctrlP2, LOW);
      digitalWrite(ctrlP3, HIGH);
      digitalWrite(ctrlP4, LOW);
      analogWrite(EN1, 255);
      analogWrite(EN2, 255);
      Serial.println("robot forward executed");
    }
    if (x ==3)
    {
      digitalWrite(ctrlP1, LOW);
      digitalWrite(ctrlP2, HIGH);
      digitalWrite(ctrlP3, LOW);
      digitalWrite(ctrlP4, HIGH);
      analogWrite(EN1, 255);
      analogWrite(EN2, 255);
      
      Serial.println("robot reverse executed");
    }
    if (x ==4)
    {
      digitalWrite(ctrlP1, LOW);
      digitalWrite(ctrlP2, LOW);
      digitalWrite(ctrlP3, HIGH);
      digitalWrite(ctrlP4, LOW);
      analogWrite(EN1, 127);
      analogWrite(EN2, 127);
      Serial.println("robot right executed");
    }
    if (x ==5)
    {
      digitalWrite(ctrlP1, HIGH);
      digitalWrite(ctrlP2, LOW);
      digitalWrite(ctrlP3, LOW);
      digitalWrite(ctrlP4, LOW);
      analogWrite(EN1, 255);
      analogWrite(EN2, 255);
      Serial.println("robot left executed");
    }
}