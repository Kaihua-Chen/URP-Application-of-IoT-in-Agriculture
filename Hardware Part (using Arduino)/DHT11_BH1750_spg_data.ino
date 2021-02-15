#include <Wire.h>
#include "Adafruit_SGP30.h"
#include "DHT.h"

Adafruit_SGP30 sgp;


//#define ADDRESS_BH1750FVI 0x23    //ADDR="L" for this module
//#define ONE_TIME_H_RESOLUTION_MODE 0x20

#define DHTPIN 8
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

#define ADDRESS_BH1750FVI 0x23    //ADDR="L" for this module
#define ONE_TIME_H_RESOLUTION_MODE 0x20

byte highByte = 0;
byte lowByte = 0;
unsigned int sensorOut = 0;
unsigned int illuminance = 0;

void setup() {
  Wire.begin();
  Serial.begin(9600);
  while (!Serial) { delay(10); } // Wait for serial console to open!

//  Serial.println("Test Begin~");
  dht.begin();

  if (! sgp.begin()){
//    Serial.println("Sensor not found :(");
//    while (1);
  }
//  Serial.print("Found SGP30 serial #");
//  Serial.print(sgp.serialnumber[0], HEX);
//  Serial.print(sgp.serialnumber[1], HEX);
//  Serial.println(sgp.serialnumber[2], HEX);

  // If you have a baseline measurement from before you can assign it to start, to 'self-calibrate'
  //sgp.setIAQBaseline(0x8E68, 0x8F41);  // Will vary for each sensor!
}

int counter = 0;
void loop() {
  Wire.beginTransmission(ADDRESS_BH1750FVI); //"notify" the matching device
  Wire.write(ONE_TIME_H_RESOLUTION_MODE);     //set operation mode
  Wire.endTransmission();
         
  delay(180);

  Wire.requestFrom(ADDRESS_BH1750FVI, 2); //ask Arduino to read back 2 bytes from the sensor
  highByte = Wire.read();  // get the high byte
  lowByte = Wire.read(); // get the low byte
     
  sensorOut = (highByte<<8)|lowByte;
  illuminance = sensorOut/1.2;
  
  //BH1750数据输出
//  Serial.print("Illum: ");
  Serial.print(illuminance); 
  Serial.print(" ");   
//  Serial.println(" lux");

  //DHT11数据输出
  float hum = dht.readHumidity();      //将湿度值赋给hum
//  Serial.print("Hum:");
  Serial.print(hum);
  Serial.print(" ");
//  Serial.print("%/t");
 
  float tem = dht.readTemperature();   //将湿度值赋给tem
//  Serial.print("    Temp:");
  Serial.print(tem);
  Serial.print(" ");
//  Serial.println("*C");

  if (! sgp.IAQmeasure()) {
//    Serial.println("Measurement failed");
    return;
  }
//  Serial.print("TVOC "); 
  Serial.print(sgp.TVOC);
  Serial.print(" ");
//  Serial.print(" ppb\t");
//  Serial.print("eCO2 "); 
  Serial.print(sgp.eCO2);
  Serial.print(" ");
//  Serial.println(" ppm");

  if (! sgp.IAQmeasureRaw()) {
//    Serial.println("Raw Measurement failed");
    return;
  }
//  Serial.print("Raw H2 "); 
  Serial.print(sgp.rawH2); 
  Serial.print(" ");
//  Serial.print(" \t");
//  Serial.print("Raw Ethanol "); 
  Serial.println(sgp.rawEthanol);
  
//  Serial.println("");

//  Serial.println("---------------------------------");
  
 
  delay(1000);

//  counter++;
//  if (counter == 30) {
//    counter = 0;

//    uint16_t TVOC_base, eCO2_base;
//    if (! sgp.getIAQBaseline(&eCO2_base, &TVOC_base)) {
//      Serial.println("Failed to get baseline readings");
//      return;
//    }
//    Serial.print("****Baseline values: eCO2: 0x"); Serial.print(eCO2_base, HEX);
//    Serial.print(" & TVOC: 0x"); Serial.println(TVOC_base, HEX);
//  }
}
