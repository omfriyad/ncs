#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h> //OLED

#include <RestClient.h>
#include <EasyButton.h>
#include <ESP8266WebServer.h>
//#include <LiquidCrystal_I2C.h>
//#include <Wire.h> 

#define OLED_RESET LED_BUILTIN  //4 SDA > D2 , SCL D1 OLED STUFF
Adafruit_SSD1306 display(OLED_RESET);

#if (SSD1306_LCDHEIGHT != 64)
#error("Height incorrect, please fix Adafruit_SSD1306.h!");
#endif


//LiquidCrystal_I2C lcd(0x27, 16, 2);   // Set the LCD address 
                                      // to 0x27 for a 16 chars 
                                      // and 2 line display

const int port = 8080;
const char* host = "192.168.1.177";

const char* ssid = "scarX";
const char* password = "1234567i";

String node_id = "id=3";
String response = "";
String call_id = "";
bool call_status = false;

RestClient client = RestClient(host,port);
ESP8266WebServer server(80);

#define BUTTON_PIN D6                   // DD6
#define BUZZER_PIN D7                  // D7
//#define LCD_P1     14                  // D5   LCD                 
//#define LCD_P2     12                  // D6 

EasyButton button(BUTTON_PIN);
bool toggle = true;
 
void onPressed() {
  if(call_status)
  {
    onpress_side();
    call_status = false;
  }
  else
  {
    clear_screen();
  }
  
   
  Serial.println("Button has been pressed!");
}


void setup() {
  Serial.begin(115200);
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  button.begin();
  button.onPressed(onPressed);
  pinMode(BUZZER_PIN, OUTPUT);

  //lcd_init();
  connection();
  route_server();
}

void loop() {
  server.handleClient();
  connection();
  button.read();
}
