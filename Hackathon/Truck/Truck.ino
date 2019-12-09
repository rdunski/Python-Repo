#include "BluetoothSerial.h"

BluetoothSerial connection;
bool stop = true;

void setup() {
  Serial.begin(9600);
  connection.begin("ESP32_Truck_Driver");
  // put your setup code here, to run once:
  pinMode(18, OUTPUT);
  pinMode(23, OUTPUT);
  pinMode(19, OUTPUT);
  pinMode(22, OUTPUT);
  pinMode(21, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (connection.available()) {
    auto received = connection.read();
    if (received == 108) {
      digitalWrite(23, HIGH); // Forward, left
      digitalWrite(18, LOW);
      stop = false;
    } else if (received == 114) {
      digitalWrite(19, HIGH); // Forward, right
      digitalWrite(22, LOW);
      stop = false;
    } else if (received == 102) {
      digitalWrite(23, HIGH); // Forward
      digitalWrite(19, HIGH);
      digitalWrite(18, LOW);
      digitalWrite(22, LOW);
      stop = false;
    } else if (received == 112) {
      digitalWrite(23, LOW); // Bacward, left
      digitalWrite(18, HIGH);
      stop = false;
    } else if (received == 115) {
      digitalWrite(19, LOW); // Backward, right
      digitalWrite(22, HIGH);
      stop = false;
    } else if (received == 98) {
      digitalWrite(23, LOW); // Backward
      digitalWrite(19, LOW);
      digitalWrite(18, HIGH);
      digitalWrite(22, HIGH);
      stop = false;
    } else if (received == 116) {
      digitalWrite(21, HIGH);
      stop = false;
    }
  }
  delay(1000);
  if (stop) {
      digitalWrite(23, LOW);
      digitalWrite(18, LOW);
      digitalWrite(19, LOW);
      digitalWrite(22, LOW);
      digitalWrite(21, LOW);
  } else stop = true;
}
