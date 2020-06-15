#include <RestClient.h>
#include <EasyButton.h>
#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN D4
#define RST_PIN D3

//const char* ssid     = "Research Lab";
//const char* password = "research12";
const char* ssid     = "scarX";
const char* password = "1234567i";

const char* host = "192.168.1.81";
const int port = 8080;

MFRC522 mfrc522(SS_PIN, RST_PIN); 
RestClient client = RestClient(host, port);
EasyButton button(D1);
String node_id = "id=1";


// Callback function to be called when the button is pressed.
void onPressed() { 
  patient_call(client,node_id);
  Serial.println("button pressed");
}

void setup() {
  
  Serial.begin(115200);
  int a = client.begin(ssid, password);
  init_server(client, node_id);

  button.begin();
  button.onPressed(onPressed);
  pinMode(D2, OUTPUT);

  SPI.begin();        // Init SPI bus
  mfrc522.PCD_Init(); // Init MFRC522
  Serial.println("RFID reading UID");
}

void loop() {
  button.read();
  read_card(mfrc522);
}
