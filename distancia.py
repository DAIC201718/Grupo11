
#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(12, GPIO.OUT)

GPIO.setup(19, GPIO.IN)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
try:
	while True:
		start = 0
		end = 0
		GPIO.output(12, False)
		time.sleep(2)
		GPIO.output(12, True)
		time.sleep(10*10**-6)
		GPIO.output(12, False)

		while GPIO.input(19) == GPIO.LOW:
			start = time.time()
#			print("Comienzo:", start)

		while GPIO.input(19) == GPIO.HIGH:
			end = time.time()
#			print("Final:", end)

		distancia = (end-start) * 343 / 2
		print ("Espacio libre:", str(distancia))

		if (distancia > 0.10):
			GPIO.output(22,GPIO.HIGH)
			print("Contenedor vacio")
			GPIO.output(21,GPIO.LOW)
			GPIO.output(17,GPIO.LOW)

		if(distancia >= 0.05) and (distancia <= 0.10):
			GPIO.output(17,GPIO.HIGH)
			print("Contenedor medio lleno")
			GPIO.output(21,GPIO.LOW)
			GPIO.output(22,GPIO.LOW)

		if (distancia < 0.05):
			GPIO.output(21,GPIO.HIGH)
			print("Contenedor lleno")
			GPIO.output(22,GPIO.LOW)
			GPIO.output(17,GPIO.LOW)

except KeyboardInterrupt:
	print("\nFin del programa")
	GPIO.output(12, False)
	GPIO.output(22,GPIO.LOW)
	GPIO.output(21,GPIO.LOW)
	GPIO.cleanup()
