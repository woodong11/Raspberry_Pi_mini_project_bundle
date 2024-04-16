# Raspberry_Pi_mini_project_bundle
<img src = "https://github.com/woodong11/Raspberry_Pi_mini_project_bundle/assets/91379630/2a806a8d-7c1b-4044-b90e-eb876ab504d9" width="40%" height="40%"><br>
라즈베리파이와 각종 센서를 이용한 미니 프로젝트 모음입니다.<br><br>
## 이용 기기 

<b>Requirement</b><br>
Raspberry Pi 5 <br><br>



## weather_pjt.py
날씨측정과 온도계를 OLED로 출력합니다.
1. 현재 온도를 BMP 280으로 얻어냅니다. (실내온도)
2. 현재 시간을 OLED에 출력합니다. (리눅스 명령어 사용)
3. REST API와 wget 명령어로 날씨 정보를 인터넷에서 얻어옵니다. (실외 온도)
<br><br>
![93BAA774-AD6D-4CA9-BE70-73DE1A893F13](https://github.com/woodong11/Raspberry_Pi_mini_project_bundle/assets/91379630/aa585531-3bf6-443e-9d09-6d3a5568306c)

<br><b>prepare for bmp 280</b><br>
$ `git clone https://github.com/pimoroni/bmp280-python` <br>
$ `cd bmp280-python`<br>
$ `sudo ./install.sh`<br>
<br><b>prepare for oled</b><br>
$ `cd ~ && mkdir oled`<br>
$ `cd ./oled`<br>
$ `wget https://files.waveshare.com/upload/2/2c/OLED_Module_Code.7z`<br>
$ `sudo apt-get install p7zip`<br>
$ `7zr x ./OLED_Module_Code.7z`<br>
$ `cd ./OLED_Module_Code/RaspberryPi/python/`<br>
$ `sudo python3 setup.py install`<br>
<br><b>oled sample test</b><br>
$ `cd ./example/`<br>
$ `python3 OLED_0in96_test.py`<br>

<br><b> get REST API key</b><br>
참고: https://icedhotchoco.tistory.com/entry/OpenWeatherMap-%EB%82%A0%EC%94%A8-API<br>

<b> run </b><br>
소스코드 change to yours! 부분에 자신의 API key, 원하는 도시로 변경합니다. <br>
$ `python3 weather_pjt.py` <br>




## mood_light.py

<img src = "https://github.com/woodong11/Raspberry_Pi_mini_project_bundle/assets/91379630/ddb89362-350b-41e5-98a0-a90f18e6e3f7" width="40%" height="40%">
<br>
red, green, blue 버튼을 눌러 자기가 원하는 색상을 만들 수 있는 무드등입니다. <br>
1. R, G, B 각 버튼을 누를수록 색상 값이 밝아집니다.
2. 한 컬러에 대해 최대 밝기가 된다면, 다시 가장 어두운 컬러로 변경됩니다.
3. SMD RGB 센서를 이용했습니다.


<br><b> run </b><br>
$ `python3 mood_light.py`


## rfid_access_system.py
<img src = "https://github.com/woodong11/Raspberry_Pi_mini_project_bundle/assets/91379630/2c262fb9-ed33-49ae-9dd3-dc035e01b6da" width="40%" height="40%">

라즈베리파이의 rfid 센서를 이용해 허가된 사용자만 출입을 허용하는 시스템입니다. <br>

1. 시스템 준비 단계: 초록 led 3번 깜빡임 후 "ready" 출력 
2. 허가된 이용자 - 출입 인증 성공:  Welcome 메시지 출력, 출입 카운팅, 파란 led 한 번 깜빡임
3. 허가된 이용자 x - 출입 실패 시: LED2 5번 빠르게 깜빡임

<br><b> ready for RFID </b><br>
$ `cd ~ && mkdir rfid` <br>
$ `cd ./rfid` <br>
$ `git clone https://github.com/pimylifeup/MFRC522-python` <br>
$ `cd ./MFRC522-python/sudo python3 setup.py install` <br>


라즈베리 파이 5는 아래의 과정을 진행해야 합니다.<br><br>
<b>MFRC522.py 편집 </b><br>
`cd ~/rfid/MFRC522-python/mfrc522`
`vi MFRC522.py`

vi로 들어가서, `import RPi.GPIO as GPIO`를 `from gpiozero import DigitalOutputDevice` 로 바꿔준다


## led_toggle.py
특정 LED를 켜고 끌 수 있는 제어 쉘을 제작합니다.
1. H/W 준비물 : LED 3개, 220옴 저항 3개
2. 만약 on 상태라면 off로, off 상태라면 on 으로 변경
<br><br>

<img src = "https://github.com/woodong11/Raspberry_Pi_mini_project_bundle/assets/91379630/db485298-eb41-480f-82b4-4e4b1a7827a1" width="40%" height="40%"><br>
<br><b> run </b><br>
$ `python3 led_toggle.py` <br>
원하는 숫자 (1~3) 중 하나 입력




## 7_segment_timing.py
타이밍에 맞춰 버튼을 누르면 불빛이 나오는 게임을 제작합니다.
1. H/W 준비물 : 7segment, 220옴 저항 3개, LED 2개, 레이저 모듈, 버튼 1개
2. FND는 0 ~ 9 까지 Up Counting -> 9 ~ 0 까지 Down Counting 진행 반복
3. 정확히 FND 숫자 7이 나오는 타이밍에 버튼을 누르면 : 연결된 LED 2개와 레이저 모두, 3초간 깜박거림
<br><br>

<img src = "https://github.com/woodong11/Raspberry_Pi_mini_project_bundle/assets/91379630/bf0fdca5-4da9-4660-b4e3-1f625d89338d" width="40%" height="40%"><br>
<br><b> run </b><br>
$ `python3 led_toggle.py`


## ikon_love_scenario.py
![image](https://github.com/woodong11/Raspberry_Pi_mini_project_bundle/assets/91379630/29ef82c7-9aed-4bc1-aa75-318aed2518f5)


<img src = "https://github.com/woodong11/Raspberry_Pi_mini_project_bundle/assets/91379630/e35f6762-c424-4442-b164-cbf21479874f" width="40%" height="40%">

<br>
사랑을 했다 노래의 첫 소절을 피에조 부저로 노래합니다.
<br><b> run </b><br>
$ `python3 ikon_love_scenario.py`


<br>








