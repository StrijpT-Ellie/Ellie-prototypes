/* Arduino pins where the LED is attached */
#define LED_GREEN 3
#define LED_RED 2
#define LED_YELLOW 1
#define sensorPin A0 // Analog input pin that the Sensor is attached to
/* boolean variables to hold the status of the pins*/
bool ledRedPinStatus = 0;
bool ledGreenPinStatus = 0;
bool ledYellowPinStatus = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_GREEN, OUTPUT);
  pinMode(LED_RED, OUTPUT);
  pinMode(LED_YELLOW, OUTPUT);
  pinMode(sensorPin, INPUT);
  Serial.begin(9600);// initialize serial communications at 9600 bps:
}

void loop() {
  // put your main code here, to run repeatedly:
  int sensorValue = analogRead(sensorPin);
  Serial.println(sensorValue);
  if (sensorValue > 555 )
  {
    ledRedPinStatus = 1;
  }
  else {
    ledRedPinStatus = 0;
  }
  if (sensorValue > 800) {
    ledGreenPinStatus = 1;
  }
  else {
    ledGreenPinStatus = 0;
  }
  if (sensorValue > 1000) {
    ledYellowPinStatus = 1;
  }
  else {
    ledYellowPinStatus = 0;
  }
  digitalWrite(LED_GREEN, ledGreenPinStatus);
  digitalWrite(LED_RED, ledRedPinStatus);
  digitalWrite(LED_YELLOW, ledYellowPinStatus);
  delay(250);
}
