
void post_request(RestClient client, String route_p, String concat_msg, int len){
  
  String response = "";
  char msg[len];
  concat_msg.toCharArray(msg, len);

  char route[20];
  route_p.toCharArray(route,20);
  int statusCode = client.post(route, msg, &response);
}



void init_server(RestClient client, String node_id){
  
  //Server Initializaion code, it will send 
  String ip_address = WiFi.localIP().toString();
  String concat_msg = "ip=" +ip_address+ "&" +node_id ;

  post_request(client, "/api/init/", concat_msg, 30);
}


void patient_call(RestClient client,String node_id){
    buzzer_sound();
    post_request(client, "/api/bed/", node_id, 10);
}
