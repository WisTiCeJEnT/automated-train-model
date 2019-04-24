#include <ESP8266WiFi.h>
#include <WiFiClient.h> 
#include <ESP8266WebServer.h>
#include <ESP8266HTTPClient.h>
const char *ssid = "room1221";  //ENTER YOUR WIFI SETTINGS
const char *password = "juiicepp";
const char *host = "http://192.168.1.25:5000/jui";
void setup() {
  pinMode(D0, OUTPUT);
  Serial.begin(9600);
  delay(1000);
  WiFi.mode(WIFI_OFF);        //Prevents reconnection issue (taking too long to connect)
  delay(1000);
  WiFi.mode(WIFI_STA);        //This line hides the viewing of ESP as wifi hotspot
  WiFi.begin(ssid, password);     //Connect to your WiFi router
  Serial.println("");
  Serial.print("Connecting");
  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
      //If connection successful show IP address in serial monitor
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());  //IP address assigned to your ESP 
  }
}

void loop() {
  HTTPClient http;    //Declare object of class HTTPClient
  http.addHeader("Content-Type", "text/plain");    //Specify content-type header
  while(!Serial.available())
  {
    Serial.println(host);
    http.begin(host);              //Specify request destination
    int httpCode = http.GET();   //Send the request
    String payload = http.getString();    //Get the response payload
    Serial.println(httpCode);   //Print HTTP return code
    Serial.println(payload);    //Print request response payload
    http.end();  //Close connection
    
    if(payload[0]=='1'){
      digitalWrite(D0, HIGH);   // turn the LED on (HIGH is the voltage level)    
    }
    else{
      digitalWrite(D0, LOW);    
    }
    delay(1000);
   } 
}
