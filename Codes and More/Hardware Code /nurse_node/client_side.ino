
void init_server(){
  String ip_address = WiFi.localIP().toString();
  String concat_info = "ip=" +ip_address+ "&" +node_id ;
  char msg[30];
  concat_info.toCharArray(msg, 30);
  int statusCode = client.post("/api/init/", msg, &response);
}

void onpress_side(){
  Serial.println("Button has been pressed!");
  print_screen("Updating the server!");
  
  //NEED TO ADD CALL ID ALONG WITH NURSE ID
  String str = node_id+"&"+call_id;
  char msg[30];
  str.toCharArray(msg, 30);
  int statusCode = client.post("/api/nurse/", msg, &response);
  //Serial.println(response);
  
  buzz();
  print_screen("Update done!");
  
  
//  lcd.clear();
//  lcd_i2c("Received",0,0);
//  delay(1000);
//  lcd.clear();
}
