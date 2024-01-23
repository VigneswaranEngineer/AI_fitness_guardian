const int muscleSensorPin = A0; // Analog pin where the muscle sensor is connected

void setup() {
  Serial.begin(9600); // Initialize serial communication for debugging
}

void loop() {
  // Read analog value from muscle sensor
  int muscleSensorValue = analogRead(muscleSensorPin);

  // Print the value to the serial monitor
  Serial.println("Muscle Sensor Reading: " + String(muscleSensorValue));

  // Send the value to the Serial Plotter
  Serial.print("M ");
  Serial.println(muscleSensorValue);

  // Add your logic for processing and controlling devices based on the sensor reading
  
  delay(1000); // Wait for a short duration before the next reading
}
