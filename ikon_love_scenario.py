from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

lst  = [261.32, 293.66, 329.62, 249.22, 391.99, 440.00, 493.88, 523.25, 587.32 ]   # 도 레 미 파 솔 라 시 도 레 

timeList = [0.3, 0.15, 0.6, 0.45]
# 4분음표,8분음표, 2분음표, 4분+ 반 

b = TonalBuzzer(14)

############### 사랑을 했다
b.play(lst[6])
sleep(timeList[0])
b.stop()
b.play(lst[5])
sleep(timeList[0])
b.stop()
b.play(lst[4])
sleep(timeList[0])
b.stop()
b.play(lst[6])
sleep(timeList[1])
b.stop()
b.play(lst[8])
sleep(timeList[3])
b.stop()

################## 우리가 만나
sleep(timeList[1])
b.play(lst[6])
sleep(timeList[0])
b.stop()
b.play(lst[5])
sleep(timeList[0])
b.stop()
b.play(lst[4])
sleep(timeList[0])
b.stop()
b.play(lst[6])
sleep(timeList[1])
b.stop()
b.play(lst[5])
sleep(timeList[3])
b.stop()

##################### 지우지 못할
sleep(timeList[1])
b.play(lst[6])
sleep(timeList[0])
b.stop()
b.play(lst[5])
sleep(timeList[0])
b.stop()
b.play(lst[4])
sleep(timeList[0])
b.stop()
b.play(lst[5])
sleep(timeList[1])
b.stop()
sleep(0.1)
b.play(lst[5])
sleep(timeList[0])
b.stop()

################# 추억이 됐다
b.play(lst[4])
sleep(timeList[1])
b.stop()
b.play(lst[5])
sleep(timeList[0])
b.stop()
b.play(lst[4])
sleep(timeList[0])
b.stop()
b.play(lst[5])
sleep(timeList[0])
b.stop()
b.play(lst[4])
sleep(timeList[2])
b.stop()
