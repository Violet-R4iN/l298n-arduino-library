
#ifndef movecore_h
#define movecore_h
#include "Arduino.h"
class movecore {

  private:
  int ctrlP1;
  int ctrlP2;
  int EN1;
  int EN2; 
  int ctrlP3; 
  int ctrlP4;

  public:
    movecore (int ENP1, int ENP2, int ENA, int ENB, int ENP3, int ENP4);
    void pinSetup();
    void sequence01(int x);
};

#endif