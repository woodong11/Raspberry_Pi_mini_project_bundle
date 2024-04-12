from gpiozero import LED
from time import sleep
#import RPi.GPIO as GPIO

led1 = LED(14) #GPIO pin number
led2 = LED(15)
led3 = LED(18)

while True:
    usrinput = int(input("INPUT>>"))
    
    if (usrinput == 1):
	    led1.toggle()
    
    elif (usrinput == 2):
	    led2.toggle()
    
    elif (usrinput == 3):
	    led3.toggle()

    else:
        print("wrong number")
        
