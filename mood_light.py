from gpiozero import PWMLED, Button
from time import sleep
from signal import pause

R = PWMLED(14)
G = PWMLED(15)
B = PWMLED(18)
R_btn = Button(17)
G_btn = Button(27)
B_btn = Button(22)

R_value, G_value, B_value = 0, 0, 0

def R_press():
    print("red button")
    global R_value
    R_value = (R_value + 1) % 10
    R.value = R_value / 10    

def G_press():
    print("green button")
    global G_value
    G_value = (G_value + 1) % 10
    G.value = G_value / 10    

def B_press():
    print("blue button")
    global B_value
    B_value = (B_value + 1) % 10
    B.value = B_value / 10    
       

R_btn.when_pressed = R_press
G_btn.when_pressed = G_press
B_btn.when_pressed = B_press

pause()
