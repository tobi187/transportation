/*
Matrix-Tastatur 3x4 Tasten klein
pin 1 : Spalte 1
pin 2 : Spalte 2
pin 3 : Spalte 3
pin 4 : Zeile 1 mit externen Pullup-Widerstand
pin 5 : Zeile 2 mit externen Pullup-Widerstand
pin 6 : Zeile 3 mit externen Pullup-Widerstand
pin 7 : Zeile 4 mit externen Pullup-Widerstand
*/
#define spalte1 13
#define spalte2 12
#define spalte3 11
#define zeile1 10
#define zeile2 9
#define zeile3 8
#define zeile4 7
#define ein LOW
#define aus HIGH
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 20, 4);  // set the LCD address to 0x27 for a 20 chars and 4 line


int f = -1;
int s = -1;
int res = -1;

int operation=-1;


void setup() {
  lcd.init();
  //lcd.backlight();
  lcd.print("0:+, 1:-, 2:*, 3:#");
  pinMode(spalte1, OUTPUT);  //Spalte 1
  pinMode(spalte2, OUTPUT);  //Spalte 2
  pinMode(spalte3, OUTPUT);  //Spalte 3
  pinMode(zeile1, INPUT_PULLUP);    //Zeile 1 mit externen Pullup-Widerstand
  pinMode(zeile2, INPUT_PULLUP);    //Zeile 2 mit externen Pullup-Widerstand
  pinMode(zeile3, INPUT_PULLUP);    //Zeile 3 mit externen Pullup-Widerstand
  pinMode(zeile4, INPUT_PULLUP);    //Zeile 4 mit externen Pullup-Widerstand
  Serial.begin(9600);
}
void loop() {
  lcd.setCursor(10, 0);  //(Spalte,Zeile)
  char cc = readkey();
  if (cc != ' ') {
    if (cc == '#') {
      printResult();
      if (res == -1) printResult();
      else {
        f = -1;
        s = -1;
        res = -1;
        lcd.setCursor(0,1);
        lcd.print("                 ");
        lcd.setCursor(0,2);
        lcd.print("                 ");
      }
    }
    if (f == -1) {
      f = cc - '0';
      lcd.setCursor(0,1);
      lcd.print(f);
    } else if (operation == -1) {
      if (cc > 4 + '0') return;
      operation = cc - '0';
      printOp();
    } else {
      s = cc- '0';
      lcd.setCursor(5,1);
      lcd.print(s);
    }
    delay(1000);
  }
}

void printOp() {
  lcd.setCursor(2,1);
  if (operation == 1) lcd.print("+");
  else if (operation == 2) lcd.print("-");
  else if (operation == 3) lcd.print("/");
  else lcd.print("/");
}

void printResult() {
  switch (operation) {
    case 1: res = f + s; break;
    case 2: res = f - s; break;
    case 3: res = f * s; break;
    case 4: res = f / s; break;
  }

  lcd.setCursor(3,3);
  lcd.print(res);
}



char readkey() {
  digitalWrite(spalte1, ein);  //Spalte 1 scannen
  digitalWrite(spalte2, aus);
  digitalWrite(spalte3, aus);
  if (digitalRead(zeile1) == 0)
    return ('*');
  else if (digitalRead(zeile2) == 0)
    return ('7');
  else if (digitalRead(zeile3) == 0)
    return ('4');
  else if (digitalRead(zeile4) == 0)
    return ('1');
  else {
    digitalWrite(spalte1, aus);  //Spalte 2 scannen
    digitalWrite(spalte2, ein);
    digitalWrite(spalte3, aus);
    if (digitalRead(zeile1) == 0)
      return ('0');
    else if (digitalRead(zeile2) == 0)
      return ('8');
    else if (digitalRead(zeile3) == 0)
      return ('5');
    else if (digitalRead(zeile4) == 0)
      return ('2');
    else {
      digitalWrite(spalte1, aus);  //Spalte 3 scannen
      digitalWrite(spalte2, aus);
      digitalWrite(spalte3, ein);
      if (digitalRead(zeile1) == 0)
        return ('#');
      else if (digitalRead(zeile2) == 0)
        return ('9');
      else if (digitalRead(zeile3) == 0)
        return ('6');
      else if (digitalRead(zeile4) == 0)
        return ('3');
      else
        return (' ');
    }
  }
}
