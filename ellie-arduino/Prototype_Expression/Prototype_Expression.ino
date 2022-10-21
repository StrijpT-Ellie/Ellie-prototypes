#define sensorPin A0

#define LED_1 7
#define LED_2 2
#define LED_3 3
#define LED_4 4
#define LED_5 5
#define LED_6 6


unsigned long lasttime = 0;

#define EMOTIONS \
  X(happy, "happy") \
  X(neutral, "neutral") \
  X(angry, "angry") \

#define X(emotion, name)

  enum emotion : size_t {
    EMOTIONS
  };

#undef X

  String ReturnEmotionText(int value) {
    if (value == 0) {
      return "happy";
    }
    else if (value == 1) {
      return "neutral";
    }
    else if (value == 2) {
      return "angry";
    }
    else {
      //code should not reach here
    }
  }


  emotion current_emotion = 1;

  emotion ProcessEmotion(int value) {
    if (value < 250) {
      current_emotion = 0;
    }
    else if (value > 350) {
      current_emotion = 2;
    }
    else {
      current_emotion = 1;
    }
    return current_emotion;
  }


  void setup() {
    // put your setup code here, to run once:
    Serial.begin(9600);
    pinMode(sensorPin, INPUT);
    pinMode(LED_1, OUTPUT);
    pinMode(LED_2, OUTPUT);
    pinMode(LED_3, OUTPUT);
    pinMode(LED_4, OUTPUT);
    pinMode(LED_5, OUTPUT);
    pinMode(LED_6, OUTPUT);
  }


  void loop() {
    // put your main code here, to run repeatedly:
    int value = analogRead(sensorPin);
    Serial.println(value);
    current_emotion = ProcessEmotion(value);
    Serial.println(ReturnEmotionText(current_emotion));
    if (current_emotion == 0) {
      digitalWrite(LED_5, HIGH);
      digitalWrite(LED_6, HIGH);
    }
    else if (current_emotion == 1) {
      digitalWrite(LED_3, HIGH);
      digitalWrite(LED_4, HIGH);
    }
    else if (current_emotion == 2) {
      digitalWrite(LED_1, HIGH);
      digitalWrite(LED_2, HIGH);
    }
    delay(200);
    digitalWrite(LED_1, LOW);
    digitalWrite(LED_2, LOW);
    digitalWrite(LED_3, LOW);
    digitalWrite(LED_4, LOW);
    digitalWrite(LED_5, LOW);
    digitalWrite(LED_6, LOW);
  }
