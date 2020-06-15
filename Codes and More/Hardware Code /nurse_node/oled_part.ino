void print_screen(String str){
 display.clearDisplay();
  display.display();

  display.setTextSize(2);
  display.setTextColor(WHITE);
  display.setCursor(0,0);
  display.println(str);
  display.display();
}

void clear_screen(){
 display.clearDisplay();
 display.display();
}
