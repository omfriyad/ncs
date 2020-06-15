
void read_card(MFRC522 mfrc522){

//  String readID = "";
  
  if ( mfrc522.PICC_IsNewCardPresent())
      {
          if ( mfrc522.PICC_ReadCardSerial())
          {
             Serial.print("Tag UID:");
//             for (byte i = 0; i < mfrc522.uid.size; i++) {
//                    Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
//                    Serial.print(mfrc522.uid.uidByte[i], HEX);
//                    readID += mfrc522.uid.uidByte[i];
//              }
              unsigned long UID_unsigned;
              UID_unsigned = mfrc522.uid.uidByte[0] << 24;
              UID_unsigned += mfrc522.uid.uidByte[1] << 16;
              UID_unsigned += mfrc522.uid.uidByte[2] << 8;
              UID_unsigned += mfrc522.uid.uidByte[3];
              
              String UID_string = (String)UID_unsigned;
              Serial.println(UID_string);
              Serial.println();
              mfrc522.PICC_HaltA();
          }
  }
  
}
