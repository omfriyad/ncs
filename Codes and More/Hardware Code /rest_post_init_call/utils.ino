
//#define BUTTON_PIN 0                        //D3
//#define PRESS_PIN 4                         //D2

//const char* ssid     = "Research Lab";
//const char* password = "research12";

void buzzer_sound(){
    
    bool toggle = true;
    
    Serial.println(toggle);
    digitalWrite(D2, toggle);
    delay(200);
    toggle=!toggle;
    digitalWrite(D2, toggle);
    Serial.println("Button has been pressed!");  
}
