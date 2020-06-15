
void route_server(){
    server.on("/",HTTP_POST, incoming);
    server.on("/alert",HTTP_POST, alert);
    server.begin();
}

void incoming() {
  Serial.println("Got One Incoming");

  String security_code = "123456789";
  if (security_code == server.arg("sc"))
  {
    Serial.println("CALLING...");
    print_screen("CALLING...");
    buzz();
    String bed_id = server.arg("bed_id");
    call_id =  "call_id=" + server.arg("call_id");
    Serial.println("Bed: "+bed_id);
    server.send(200, "text/plain", "success");
    call_status = true;
    return;
  }
  server.send(200, "text/plain", "404");
}


void alert() {
  Serial.println("Got One Alert!");

  String security_code = "123456789";
  if (security_code == server.arg("sc"))
  {
    buzz();
    String msg = server.arg("msg");
    print_screen(msg);
    server.send(200, "text/plain", "success");
    return;
  }
  server.send(200, "text/plain", "404");
}
