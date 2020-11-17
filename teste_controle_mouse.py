import pyautogui
import keyboard
import requests
import socket
import serial
import re #regx

def mouse_teclado():
    MOUSE_TIME=0.00
    largura, altura= pyautogui.size()
    MOUSE_MIN_H=largura/40
    MOUSE_MIN_V=altura/40
    pyautogui.FAILSAFE = False
    print(largura, altura)
    #centraliza
    pyautogui.moveTo(largura/2, altura/2, duration = 0.5, tween = pyautogui.easeOutQuad)
    while(not(keyboard.is_pressed('s'))):
        if keyboard.is_pressed("left arrow"):  # if key 'q' is pressed 
            pyautogui.move(-MOUSE_MIN_H, 0, MOUSE_TIME)  
        if keyboard.is_pressed("right arrow"):
            pyautogui.move(MOUSE_MIN_H, 0, MOUSE_TIME)
        if keyboard.is_pressed("up arrow"):
            pyautogui.move(0, -MOUSE_MIN_V, MOUSE_TIME)
        if keyboard.is_pressed("down arrow"):
            pyautogui.move(0, MOUSE_MIN_V, MOUSE_TIME)
        if keyboard.is_pressed("0"):
            pyautogui.click()  

def Request_Blink():

    auth_token = "lh-Y66OTh4k-_laDnmFeRIOBKyHE5z5O"
    blynk_server = socket.gethostbyname("blynk-cloud.com") # pega o ip automaticamente
    pinled = 'V13'
    pin = 'V77'
    
    #liga o led
    requests.get('http://'+blynk_server+'/'+auth_token+'/update/'+pinled+'?value=1')
    r = requests.get('http://'+blynk_server+'/'+auth_token+'/get/'+pin)
    print(r.text)
    
def mouse_sensor():
    MOUSE_TIME=0.00
    largura, altura= pyautogui.size()
    MOUSE_MIN_H=largura/40
    MOUSE_MIN_V=altura/40
    pyautogui.FAILSAFE = False
    print(largura, altura)
    #centraliza
    pyautogui.moveTo(largura/2, altura/2, duration = 0.5, tween = pyautogui.easeOutQuad)
    ser = serial.Serial('COM3', 9600)
    while(not(keyboard.is_pressed('s'))):
        bruto=str(ser.readline())
        dist=int(re.sub("\D", "", bruto))
        print(dist)
        if (dist<5):
            pyautogui.move(0, -MOUSE_MIN_V, MOUSE_TIME)
         

def serial_teste():
    ser = serial.Serial('COM3', 9600)
    while(True):
        bruto=str(ser.readline())
        char=re.sub("\D", "", bruto)
        print(int(char))


#Request_Blink()
#mouse()
#serial_teste()
mouse_sensor()