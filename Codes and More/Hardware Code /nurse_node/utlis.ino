
void connection(){
  if(WiFi.status() != WL_CONNECTED){
    print_screen("Connecting...");
    int a = client.begin(ssid,password);
    
    
    if(WiFi.status() == WL_CONNECTED){
      init_server();
      Serial.println("Initialization Done");
      print_screen("Initialization Done");
    }
  }
}

void buzz(){
  digitalWrite(BUZZER_PIN, true);
  delay(300);
  digitalWrite(BUZZER_PIN, false);
}
