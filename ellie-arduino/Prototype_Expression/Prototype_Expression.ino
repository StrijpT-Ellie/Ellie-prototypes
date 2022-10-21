unsigned long lasttime = 0;

String receivedCommunication = "none";

enum emotion {
  happy,
  neutral,
  angry
};

emotion current_emotion = neutral;

String ReceiveCommunication() {
  String receivedMessage;
  if (Serial.available()) {
    receivedMessage = Serial.readStringUntil('\n');
  }
  return receivedMessage;
}

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);// initialize serial communications at 9600 bps:
}

void loop() {
  receivedCommunication = ReceivedCommunication();
  Serial.println(receivedCommunication);
}
