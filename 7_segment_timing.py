from gpiozero import LED, Button
from time import sleep
from signal import pause

a = LED(5)
b = LED(6)
c = LED(13)
d = LED(19)
e = LED(26)
f = LED(16)
g = LED(20)
dp = LED(21)

lazer= LED(23)
led1 = LED(14)
led2 = LED(15)
btn = Button(18)

fnd =[
        [1, 1, 1, 1, 1, 1, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 0, 1, 0],
        [1, 1, 1, 1, 0, 0, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [1, 0, 1, 1, 0, 1, 1, 0],
        [1, 0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 0, 1, 1, 0]
        ]
segment = [a, b, c, d, e, f, g, dp]

def display(digit):
    for i in range(len(segment)):
        if ( fnd[digit][i] == 1):
            segment[i].on()
            
        else:
            segment[i].off()
    
def press():
    for i in range(3):
        lazer.on()
        led1.on()
        led2.on()
        sleep(0.2)
        lazer.off()
        led1.off()
        led2.off()
        sleep(0.2)

while(1):
    for i in range(10):
        display(i)
        if(i == 7 and btn.is_pressed):
            press()
        else:
            sleep(0.4)
        

    for i in range(8, 0, -1):
        display(i)
        if(i == 7 and btn.is_pressed):
            press()
        else:
            sleep(0.4)

