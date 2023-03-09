#include <movecore.h> //including library that we made before to control movement
#include <IRremote.h>  //including library to read IRdata
#include <ezButton.h> //including library to read limit switch data
#define receiver 7 
#define receiver 8
int Target = 10;
int Target_B = 100;
int IrData = 0 ;
int movedata = 0;
unsigned long time_passed;
ezButton limitSwitch(11);
ezButton wallSwitch(6);
IRrecv irrecv(receiver2);
IRrecv irrecv(receiver);
decode_results results;
movecore movecore(2,3,9,10,4,5);
void setup(){
  time_passed = millis();
  irrecv.enableIRIn();
  enableLEDFeedback();
  limitSwitch.setDebounceTime(50);
  wallSwitch.setDebounceTime(50);
  Serial.begin(9600);
  Serial.println("init");
  movecore.pinSetup();
}
int IrCore()
{
    if (IrReceiver.decode())
    IrData=IrReceiver.decodedIRData.command;
    IrReceiver.resume();
    delay(200); 
    return IrData;
   }
int Limit(){
  limitSwitch.loop();
  wallSwitch.loop();
   int state = limitSwitch.getState();
   int Wstate = wallSwitch.getState();
  if(state == LOW){
    Target = Target_B;
    Serial.println(Target);}
  if(state == HIGH){
    Target = 10;
   Serial.println(Target);}
 if(Wstate == LOW){
    movecore.sequence01(3);
    Serial.println("wall pressed");}
}
int Search(int x){
  if (x == 1);{
    Serial.println("searching Target");
    movecore.sequence01(4);
    }
  }
void loop(){
Limit();
 if(millis()-time_passed > 1000) {
   time_passed = millis(); 
    IrData = 0; }
   Serial.println(IrCore());
 if(IrCore() == Target){
    Serial.print("Target :");
    Serial.println(Target);
    Serial.println("engaging");
    movecore.sequence01(2);
  }
 if(IrCore() != Target){
    Search(1);
   }
 }
