//void lcd_init(){
//  Wire.begin(LCD_P1,LCD_P2);
//  lcd.begin();
//  lcd_print();
//}
//
//void lcd_print(){
//  lcd_i2c("Hello To",0,0);
//  lcd_i2c("NCS",0,1);
//}
//
//void lcd_i2c(String msg,int start_pos,int col){
//  lcd.setCursor(start_pos, col);
//  lcd.print(msg);
//}
//
//void lcd_buzz(){
//  
//  lcd.clear();
//  
//  String msg = "Calling";
//  lcd_i2c(msg,0,0);
//  
//}
