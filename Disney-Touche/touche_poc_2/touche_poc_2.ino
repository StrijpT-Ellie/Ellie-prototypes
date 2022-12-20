
#define range 160

float data[range];


void setFreq(int d){
  if (d<0){
    d=-d;
  }

  if (d<2){
    d=2;
  }

  TCCR1B &= 0xFE; //stop generator
  TCNT1 = 0;      //Clear generator
  ICR1 = d;
  OCR1A = (d/2);
  TCCR1B |= 0x01; //Start generator
}

void setup() {
  // put your setup code here, to run once:
  
  TCCR1A=0b10000010;        //-Set up frequency generator
  TCCR1B=0b00011001;        //-+
  setFreq(16);         //-Start with 1MHz
  pinMode(9,OUTPUT);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  for (int i = 0; i < range; i++){
    setFreq(i);
    data[i] = analogRead(0);
    Serial.print(i);
    Serial.print(":");
    Serial.println(data[i]);
  }
  delay(100);
}
