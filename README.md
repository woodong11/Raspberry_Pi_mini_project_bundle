# Raspberry_Pi_mini_project_bundle
<img src = "https://github.com/woodong11/Raspberry_Pi_mini_project_bundle/assets/91379630/2a806a8d-7c1b-4044-b90e-eb876ab504d9" width="40%" height="40%"><br>
라즈베리파이와 각종 센서를 이용한 미니 프로젝트 모음입니다.<br><br>
## 이용 기기 

<b>Requirement</b><br>
Raspberry Pi 5 <br><br>
<b>Option</b><br>
BMP280(온도,기압센서), SPI용 OLED(Waveshare사 제품), lazer



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




