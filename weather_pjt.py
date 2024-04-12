#!/usr/bin/python
# -*- coding:utf-8 -*-


################ change to yours! ##################
api_key = "your key"
city = "Busan"
#####################################################


import sys
import os

picdir = os.path.join(os.path.expanduser("~"), 'oled', 'OLED_Module_Code', 'RaspberryPi', 'python', 'pic')
libdir = os.path.join(os.path.expanduser("~"), 'oled', 'OLED_Module_Code', 'RaspberryPi', 'python', 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
import time
import traceback
from waveshare_OLED import OLED_0in96
from PIL import Image, ImageDraw, ImageFont
from bmp280 import BMP280
from smbus import SMBus
from time import sleep
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)

bus = SMBus(1)
bmp280 = BMP280(i2c_dev=bus)


########## API를 사용하고 싶지 않다면 해당 부분을 모두 주석처리합니다 ########
# whether API
import requests
def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data
##########################################################################


def translate_weather_status(status):
    translations = {
        'clear sky': '맑음',
        'few clouds': '구름 조금',
        'scattered clouds': '구름',
        'broken clouds': '부분적으로 흐림',
        'overcast clouds': '흐림',
        'mist': '안개',
        'shower rain': '소나기',
        'rain': '비',
        'thunderstorm': '천둥 번개',
        'snow': '눈',
        'mist': '안개',
        'haze': '안개',
    }
    return translations.get(status, status)


try:
    ########## API를 사용하고 싶지 않다면 해당 부분을 모두 주석처리합니다 ########
    weather_data = get_weather(api_key, city)
    # print("날씨 정보:", weather_data)
    # 도시 이름 추출
    city_name = weather_data['name']

    # 온도 추출
    temperature = round(weather_data['main']['temp'], 1)

    # 날씨 상태 추출
    weather_status = weather_data['weather'][0]['description']
    translated_weather_status = translate_weather_status(weather_status)

    print("information by openwheater:")
    print(f"도시: {city_name}")
    print(f"온도: {temperature}°C")
    print(f"날씨 상태: {weather_status} : {translated_weather_status}")
    city_temper = city_name + " " + translated_weather_status + " " + str(temperature) + "°C"
    print(city_temper)
    ##########################################################################
    
    disp = OLED_0in96.OLED_0in96()
    
    logging.info("\r 0.96inch OLED ")
    # Initialize library.
    disp.Init()
    # Clear display.
    logging.info("clear display")
    disp.clear()
    
    temper = bmp280.get_temperature()
    pres = bmp280.get_pressure()
    now = datetime.now()
    current_time = now.strftime("%p %I:%M:%S")
    local_temper = '현재 온도: {:.1f}°C'.format(temper)
    
    print(local_temper)
    
    # Create blank image for drawing.
    image1 = Image.new('1', (disp.width, disp.height), "WHITE")
    draw = ImageDraw.Draw(image1)
    font1 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 16)
    font2 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 14)
    logging.info("***draw line")
    draw.line([(0, 0), (127, 0)], fill=0)
    draw.line([(0, 0), (0, 63)], fill=0)
    draw.line([(0, 63), (127, 63)], fill=0)
    draw.line([(127, 0), (127, 63)], fill=0)
    logging.info("***draw text")
    draw.text((20, 0), current_time, font=font1, fill=0)
    draw.text((5, 24), local_temper, font=font2, fill=0)


    ########## API를 사용하고 싶지 않다면 해당 부분을 모두 주석처리합니다 ########
    draw.text((5, 38), city_temper, font=font2, fill=0)
    ##########################################################################
    
    
    image1 = image1.rotate(0)
    disp.ShowImage(disp.getbuffer(image1))
    time.sleep(5)
    
    logging.info("***draw image")
    Himage2 = Image.new('1', (disp.width, disp.height), 255)  # 255: clear the frame
    bmp = Image.open(os.path.join(picdir, '0in96.bmp'))
    Himage2.paste(bmp, (0, 0))
    Himage2 = Himage2.rotate(0)
    disp.ShowImage(disp.getbuffer(Himage2))
    time.sleep(2)
    disp.clear()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    disp.module_exit()
    exit()
