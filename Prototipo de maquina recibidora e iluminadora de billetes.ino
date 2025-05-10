#include <Servo.h>
#include <LiquidCrystal_I2C.h>
//Código de una maquina recibidora de billetes que avienta luz para poder observar las caracteristicas de seguridad y tomar una foto de manera independiente
// Definición de pines y variables
int led = 6; // Pin del LED
Servo miservo; // Objeto del servomotor
LiquidCrystal_I2C lcd(0x27, 16, 2); // Pantalla LCD I2C
String mensaje = ""; // Variable para recibir mensajes desde la computadora

void setup() {
  // Configuración inicial
  lcd.init();
  lcd.clear();         
  lcd.backlight();
  lcd.setCursor(2, 0); 
  lcd.print("Insertando...");

  miservo.attach(9); // Asociar servomotor al pin 9
  miservo.write(90);  // Inicia en 90°
  delay(1000);
  miservo.write(0); 
  delay(1000);

  lcd.clear();
  lcd.setCursor(2, 0);
  lcd.print("Inserte billete");

  pinMode(led, OUTPUT);
  Serial.begin(9600); 
}

void loop() {
  if (Serial.available()) {
    char tecla = Serial.read(); // Leer la tecla ingresada
    if (tecla == 'p') { 
      miservo.write(90);
      delay(1000);
      
      digitalWrite(led, HIGH);

      // Mostrar "Analizando..."
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Analizando...");

      // Limpiar el buffer serial antes de leer
      while (Serial.available()) {
        Serial.read();
      }

      // Esperar mensaje con un tiempo límite
      unsigned long startTime = millis();
      mensaje = ""; 
      while (millis() - startTime < 20000) { // Esperar hasta 5 segundos
        if (Serial.available()) {
          mensaje = Serial.readStringUntil('\n'); // Leer hasta el final de línea
          mensaje.trim(); // Limpiar espacios
          break; // Salir si recibimos algo
        }
      }

      // Decidir la acción según el mensaje recibido
      if (mensaje == "verdadero") {
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Resultado:");
        lcd.setCursor(0, 1);
        lcd.print("Verdadero");
      } else if (mensaje == "falso") {
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Resultado:");
        lcd.setCursor(0, 1);
        lcd.print("Falso");
      } else if (mensaje == "") { 
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Error:");
        lcd.setCursor(0, 1);
        lcd.print("Sin respuesta");
      } else {
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Resultado:");
        lcd.setCursor(0, 1);
        lcd.print("No legible");
      }
      
      delay(2000); 

      digitalWrite(led, LOW);
      miservo.write(0);
      delay(1000);

      lcd.clear();
      lcd.setCursor(2, 0);
      lcd.print("Inserte billete");
    }
  }
}
