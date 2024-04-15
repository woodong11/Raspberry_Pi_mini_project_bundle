from mfrc522 import SimpleMFRC522
from gpiozero import LED
from time import sleep

dongwooKey = 672495319008    # change to your RFID key
allowKey = []
FND = 0                      # counting 

green = LED(14)
blue = LED(15)
red = LED(18)

# ready
allowKey.append(dongwooKey)     # 원하는 키들 추가하기
for _ in range(3):
    green.on()
    sleep(0.3)
    green.off()
    sleep(0.3)
print("Ready")
green.on()

# run
while True:
    print('Tag your Card!')
    id = SimpleMFRC522().read()[0]
    print("check id: ", id)
    
    if id in allowKey:
        print("{id} : Welcome")
        FND += 1
        blue.on()
        sleep(0.5)
        blue.off()
        sleep(0.5)

    else:
        print("You are not allowed")
        for _ in range(5):
            red.on()
            sleep(0.1)
            red.off()
            sleep(0.1)
        
    sleep(0.3)
