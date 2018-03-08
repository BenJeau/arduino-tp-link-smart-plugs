const int SW_pin = 2;
const int X_pin = 0;
const int Y_pin = 1;

boolean check1 = false;
boolean check2 = false;
boolean check3 = false;

void setup() {
  pinMode(SW_pin, INPUT);
  digitalWrite(SW_pin, HIGH);
  Serial.begin(9600);
}

void loop() {
  int a = digitalRead(SW_pin);
  int b = analogRead(Y_pin);  
  
  if (a == 0 && !check1) {
    check1 = true;
    Serial.print("1");
  } else if (a == 1 && check1) {
    check1 = false;
  } 
  
  if (b == 0 && !check2) {
    check2 = true;
    Serial.print("2");
  } else if (b == 1023 && !check3) {
    check3 = true;
    Serial.print("3");
  } else if (b > 500 && check2) {
    check2 = false;
  } else if (b < 523 && check3) {
    check3 = false;
  }
}
