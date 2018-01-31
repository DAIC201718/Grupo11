import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

while True:
	GPIO.output(17, GPIO.HIGH)
	print("Roja encendida")
	time.sleep(1)
	GPIO.output(17, GPIO.LOW)
	print("Roja apagada")
	time.sleep(1)

GPIO.cleanup()

#17 naranja
#21 rojo
#22 verde
