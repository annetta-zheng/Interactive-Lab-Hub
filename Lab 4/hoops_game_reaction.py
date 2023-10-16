from __future__ import print_function, division
import random
import qwiic_led_stick
import sys
import board
from adafruit_apds9960.apds9960 import APDS9960
import busio
import qwiic_oled_display
import time
from time import sleep
import math
import qwiic_proximity
import qwiic_twist
from rainbowio import colorwheel
from adafruit_seesaw.seesaw import Seesaw
from adafruit_seesaw.analoginput import AnalogInput
from adafruit_seesaw import neopixel

from Qwiic_LED_Stick_examples.qwiic_led_stick_ex8_walking_rainbow import walking_rainbow 

i2c = busio.I2C(board.SCL, board.SDA)
########### apds9960 ##########################
apds = APDS9960(i2c)
apds.enable_proximity = True
####### Distance Sensor #######################
oProx = qwiic_proximity.QwiicProximity()
if oProx.begin() == False:
    print("The Qwiic Proximity device isn't connected to the system. Please check your connection", \
        file=sys.stderr)
########### LEDStick ##########################
my_stick = qwiic_led_stick.QwiicLEDStick()
if my_stick.begin() == False:
    print("\nThe Qwiic LED Stick isn't connected to the sytsem. Please check your connection", \
        file=sys.stderr)
########### NEOslider #########################
neoslider = Seesaw(i2c, 0x30)
potentiometer = AnalogInput(neoslider, 18)
pixels = neopixel.NeoPixel(neoslider, 14, 4, pixel_order=neopixel.GRB)

print("sensor init complete")

def potentiometer_to_color(value):
    """Scale the potentiometer values (0-1023) to the colorwheel values (0-255)."""
    return value / 1023 * 255

def neo_slider():
    print(potentiometer.value)
    # Fill the pixels a color based on the position of the potentiometer.
    pixels.fill(colorwheel(potentiometer_to_color(potentiometer.value)))
    
def blink(t = 1):
        for i in range(0, t+1):
            my_stick.set_all_LED_brightness(0)
            time.sleep(0.1)
            my_stick.set_all_LED_brightness(32)
            time.sleep(0.1)
        my_stick.set_all_LED_brightness(6)
def display_LED(add_who, p1_score, p2_score):
    total_score = p1_score + p2_score
    print('1', p1_score, '2', p2_score)
    if total_score >= 10:
        if p1_score > p2_score:
            # Yellow to green
            for r in range(255, 0, -1):
                my_stick.set_all_LED_color(r, 255, 0)
                sleep(0.01)
            my_stick.set_all_LED_color(0, 128, 0)
        elif p2_score > p1_score:
            # Magenta to red
            for b in range(255, 0, -1):
                my_stick.set_all_LED_color(255, 0, b)
                sleep(0.01)
            my_stick.set_all_LED_color(255, 0, 0)
        else:
            walking_rainbow(my_stick, 20, 10, 0.1)
        blink(3)
    else:
        if add_who == 1:
            green_list[total_score - 1] = 128
        if add_who == 2:
            red_list[total_score - 1] = 255
        my_stick.set_all_LED_unique_color(red_list, green_list, blue_list, LED_length)
        blink()
def display_LED_lose(minus_who_p, p1_score, p2_score):
    print('1', p1_score, '2', p2_score)
    if p1_score >= 5 or p2_score >= 5:
        if p2_score == 5:
            # Yellow to green
            for r in range(255, 0, -1):
                my_stick.set_all_LED_color(r, 255, 0)
                sleep(0.01)
            my_stick.set_all_LED_color(0, 128, 0)
        else:
            # Magenta to red
            for b in range(255, 0, -1):
                my_stick.set_all_LED_color(255, 0, b)
                sleep(0.01)
            my_stick.set_all_LED_color(255, 0, 0)
        blink(3)
    else:
        if minus_who_p == 0:
            green_list[p1_score - 1] = 0
        if minus_who_p == 1:
            red_list[4+p2_score] = 0
        print('s',red_list, green_list, blue_list)
        my_stick.set_all_LED_unique_color(red_list, green_list, blue_list, LED_length)
        blink()        
def get_random_player():
    r, g, b = [0] * 10, [0] * 10, [0] * 10
    p = random.randint(0, 1)
    if p == 0:
        g[4] = 128
        g[5] = 128
    else:
        r[4] = 255
        r[5] = 255
    # print(r,g,b)
    my_stick.set_all_LED_unique_color(r, g, b, LED_length)
    time.sleep(1)
    my_stick.set_all_LED_unique_color([0] * LED_length, [0] * LED_length, [0] * LED_length, LED_length)
    return p
def init_rgb():
    red_list = [0] * LED_length
    green_list = [0] * LED_length
    blue_list = [0] * LED_length
    for i in range(10):
        if i < 5:
            green_list[i] = 128
        else:
            red_list[i] = 255
    return red_list, green_list, blue_list
# Initialize Variables
walking_rainbow(my_stick, 20, 10, 0.1)
p1_score = 0
p2_score = 0
LED_length = 10
red_list, green_list, blue_list = init_rgb()
my_stick.set_all_LED_unique_color(red_list, green_list, blue_list, LED_length)
print("game starts now")
print('s',red_list, green_list, blue_list)
while True:
    try:
        t0 = time.time()
        p = get_random_player()
        game_time = random.randint(3, 10)
        is_score = False
        while math.floor(time.time() - t0) < game_time:
            countdown = game_time - math.floor(time.time() - t0)
            p1_prox = apds.proximity
            p2_prox = oProx.get_proximity()
            # print(time.time())
            if p == 0:
                if p1_prox > 5:
                    is_score = True
                    break
            if p == 1:
                if p2_prox > 75:
                    is_score = True
                    break
            sleep(0.1)
        my_stick.set_all_LED_unique_color(red_list, green_list, blue_list, LED_length)
        print(p, is_score, p1_score, p2_score)
        if is_score == False:
            if p == 0:
                p1_score +=1
            else:
                p2_score +=1
            display_LED_lose(p, p1_score, p2_score)
        # print(potentiometer.value / 1023 * 255)
        sleep(0.1)
    except KeyboardInterrupt: 
        break   

