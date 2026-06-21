

int ledPin=2;
char gelenVeri;

void setup() {
 Serial.begin(9600);
 pinMode(ledPin,OUTPUT);


}


void loop() {
  if(Serial.available()>0)
  {
    gelenVeri=Serial.read();
    if(gelenVeri=='a') digitalWrite(ledPin,HIGH);
    else if(gelenVeri=='b')digitalWrite(ledPin,LOW);
  }
}