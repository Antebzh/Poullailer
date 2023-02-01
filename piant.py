
#!/usr/bin/env python3

import os
import time
import sys
import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BOARD) #Définit le mode de numérotation (Board)
GPIO.setwarnings(False) #On désactive les messages d'alerte

#liste des GPIOs utilisés
gpio=[12,16,18,22,32,36,38,40,37,35,33,31,29,15,11,13]

arg1 = ( sys.argv[1] )
delay = int( sys.argv[2] )
for x in range(len(gpio)):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(gpio[x], GPIO.OUT,initial = GPIO.HIGH)

def ferme(delay):

	print("Fermeture")
	GPIO.output(gpio[10-1], GPIO.LOW)
	GPIO.output(gpio[9-1], GPIO.LOW)
	time.sleep(delay)
	GPIO.output(gpio[9-1], GPIO.HIGH)
	GPIO.output(gpio[10-1], GPIO.HIGH)

def ouvre(delay):
	print("Ouverture")
	GPIO.output(gpio[12-1], GPIO.LOW)
	GPIO.output(gpio[11-1], GPIO.LOW)
	time.sleep(delay)
	GPIO.output(gpio[12-1], GPIO.HIGH)
	GPIO.output(gpio[11-1], GPIO.HIGH)

def set_gpio(num,delay):
	GPIO.output(gpio[num-1], GPIO.LOW)
	time.sleep(delay)
	GPIO.output(gpio[num-1], GPIO.HIGH)


if arg1 =="ouvre":
	ouvre(delay)
elif arg1=="ferme":
	ferme(delay)

else :

	num=int(arg1)
	set_gpio(num,delay)



GPIO.cleanup()
