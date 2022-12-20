#define steps 160

float results[steps];


void average(){
  float moving_average[steps];
  for (int i = 0; i < steps; i++){
    if (i < 5){
      moving_average[i] = results[i];
    }
    else{
      float total = 0;
      for (int j = 2; j > 0; j--){
        total = total + results[i-j];
      }
      moving_average[i] = total/3;
    }
    Serial.print(i);
    Serial.print(":");
    Serial.println(moving_average[i]);
  }
}


void setup() {
  // put your setup code here, to run once:
  pinMode(9, OUTPUT);
  TCCR1A = 0;
  TCCR1B = 0;

  TCCR1A |= (1 << COM1A0);
  TCCR1B |= (1 << WGM12);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  for (int i = 0; i < steps; i++){
    TCCR1B &= 0xFE;
    TCNT1 = 0;
    OCR1A = i;
    TCCR1B |= 0x01;

    results[i] = analogRead(0);
    Serial.print(i);
    Serial.print(":");
    Serial.println(analogRead(0));
  }
  //average();
  
}
