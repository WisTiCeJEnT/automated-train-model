#include <ESP8266WiFi.h>
#include <WiFiClient.h> 
#include <ESP8266WebServer.h>
#include <ESP8266HTTPClient.h>
#define R D0
#define G D1
#define B D2
#define buzzerPIN D3
#define LED7 D4
#define clkLED7 D5
#define backLEDPIN D7
#define frontLEDPIN D8

const char *ssid = "room1221";  //ENTER YOUR WIFI SETTINGS
const char *password = "juiicepp";
const char *host = "http://192.168.1.25:5000/train";

void setup() {
  pinMode(R, OUTPUT);
  pinMode(G,OUTPUT);
  pinMode(B,OUTPUT);
  pinMode(buzzerPIN,OUTPUT);
  pinMode(backLEDPIN,OUTPUT);
  pinMode(frontLEDPIN,OUTPUT);

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

    char movement=payload[0];
    char source=payload[2];
    char dest=payload[3];
    char horn=payload[1];
 
    if(movement=='0'){
      digitalWrite(frontLEDPIN, LOW);
      digitalWrite(backLEDPIN, LOW);
      Serial.println("Stopping");
    }
    else if(movement=='1'){
      digitalWrite(frontLEDPIN, HIGH);
      digitalWrite(backLEDPIN, LOW);
      Serial.println("Forward");
    }
    else if(movement=='2'){
      digitalWrite(frontLEDPIN, LOW);
      digitalWrite(backLEDPIN, HIGH);
      Serial.println("Reversed");
    }


    if(horn=='1'){
      tone(buzzerPIN,100);
      Serial.println("Beep !");
    }
    else if(horn=='0'){
      tone(buzzerPIN,0);
      Serial.println("Sleep Zzz...");
    }
    delay(1000);
   } 
}
