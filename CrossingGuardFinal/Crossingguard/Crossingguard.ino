
int incomingByte; // a variable to read incoming serial data into

void setup() {
  
  Serial.begin(9600);
  
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
}

void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    
    incomingByte = Serial.read();
    
    if (incomingByte == 'S') {
      digitalWrite(13, HIGH);
      digitalWrite(12, LOW);
    }
    
    if (incomingByte == 'G') {
      digitalWrite(13, LOW);
      digitalWrite(12, HIGH);
    }
  }
}
