const int muscleSensorPin = A0; // Analog pin where the muscle sensor is connected

void setup() {
  Serial.begin(115200); // Initialize serial communication for debugging
  while(!Serial){}
}

void loop() {
  // Read analog value from muscle sensor
  int muscleSensorValue = analogRead(muscleSensorPin);
  
  delay(1000); // Wait for a short duration before the next reading
}
