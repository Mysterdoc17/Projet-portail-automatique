#include <deprecated.h>
#include <MFRC522.h>
#include <MFRC522Extended.h>
#include <SPI.h>
byte nuidPICC[4];
#define RST_PIN 9
#define SS_PIN 10

int SDA = 10;
int SCK = 13;

MFRC522 maquette_portail(SS_PIN, RST_PIN);


void setup() {
  Serial.begin(9600);
  SPI.begin();
  maquette_portail.PCD_Init();
  maquette_portail.PCD_DumpVersionToSerial();
  Serial.println(F('Scannez le PICC pour voir UID...'));
  
}

void loop() 
{
  // Attente d'une carte RFID
  if(!maquette_portail.PICC_IsNewCardPresent())
  {
    return;
  }
  if (maquette_portail.uid.uidByte[0] != nuidPICC[0] || 
    maquette_portail.uid.uidByte[1] != nuidPICC[1] || 
    maquette_portail.uid.uidByte[2] != nuidPICC[2] || 
    maquette_portail.uid.uidByte[3] != nuidPICC[3] ) 
    Serial.println(F("A new card has been detected."));

    // Store NUID into nuidPICC array
    for (byte i = 0; i < 4; i++) {
      nuidPICC[i] = maquette_portail.uid.uidByte[i];
  }
  // Récupération des informations de la carte RFID
  if(!maquette_portail.PICC_ReadCardSerial())
  {
    return;
  }
  //affichage des informations de la carte RFID
  maquette_portail.PICC_DumpToSerial(&(maquette_portail.uid));
}
