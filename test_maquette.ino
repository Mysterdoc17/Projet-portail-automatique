int moteur1 = 2;
int moteur2 = 3;
int capteur1_FDC = 4;
int capteur2_FDC = 5;

void setup() {
  Serial.begin(9600);
  pinMode(capteur1_FDC, INPUT);
  pinMode(moteur1, OUTPUT);
  pinMode(moteur2, OUTPUT);
}
void ouverture()
{
  // ouvrir le portail juqu'au capteur de fin de course
  while ((digitalRead(capteur1_FDC)) != HIGH)
  {
    digitalWrite(moteur1, HIGH);
    digitalWrite(moteur2, LOW);
  }
  digitalWrite(moteur1, LOW);
  digitalWrite(moteur2, LOW);
}

void fermeture()
{
  // fermer le portail jusqu'au capteur de fin de course
  while ((digitalRead(capteur2_FDC)) != HIGH)
  {
    digitalWrite(moteur1, LOW);
    digitalWrite(moteur2, HIGH);
  }
  digitalWrite(moteur1, LOW);
  digitalWrite(moteur2, LOW);
}

void loop() {
  ouverture();
  delay(1000);
  fermeture();
}
