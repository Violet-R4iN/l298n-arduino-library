#include <SoftwareSerial.h>
#include <movecore.h>
SoftwareSerial EEBlue(0, 1); // RX | TX
movecore movecore(4, 5, 6, 8, 9, 10);
char flag;
int SPD = 255;
void setup()
{
 
  Serial.begin(9600);
  EEBlue.begin(9600);  //Default Baud for comm, it may be different for your Module.
  movecore.pinSetup(); 
 
}
 
void loop()
{
 
  // Feed any data from bluetooth to Terminal.
  if (EEBlue.available())
   {
    flag = EEBlue.read();
    Serial.println(flag);
   }
   switch (flag)
  {
    case 'a':
      //Serial.println("Forward");
      movecore.sequence01(1 ,SPD);
      break;

    case 'b':
      //Serial.println("Reverse");
      movecore.sequence01(2 ,SPD);
      break;

    case 'c':
      //Serial.println("Left");
      movecore.sequence01(4 ,SPD);
      break;

    case 'd':
      //Serial.println("Right");
      movecore.sequence01(3 ,SPD);
      break;

    case 'e':
      //Serial.println("Stop");
      movecore.sequence01(0,0);
      break;
  }
}
