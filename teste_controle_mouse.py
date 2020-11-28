import pyautogui  # Controla o Mouse e teclado
import keyboard  # Pega os dados do Teclado instantaneamente
import requests  # faz requests http
from socket import gethostbyname  # requisição DNS Automatica
import serial  # comunicação serial com a Wemos
import re  # regx


def mouse_teclado():
    MOUSE_TIME = 0.00
    largura, altura = pyautogui.size()
    MOUSE_MIN_H = largura/40
    MOUSE_MIN_V = altura/40
    pyautogui.FAILSAFE = False
    print(largura, altura)
    # centraliza
    pyautogui.moveTo(largura/2, altura/2, duration=0.5,
                     tween=pyautogui.easeOutQuad)
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
    # pega o ip automaticamente
    blynk_server = gethostbyname("blynk-cloud.com")
    pinled = 'V77'
    pin = 'V77'

    # liga o led
    requests.get('http://'+blynk_server+'/' +
                 auth_token+'/update/'+pinled+'?value=U')
    r = requests.get('http://'+blynk_server+'/'+auth_token+'/get/'+pin)
    bruto = str(r.text)
    char = re.sub("\D", "", bruto)
    print(char)


def mouse_sensor():
    MOUSE_TIME = 0.00
    largura, altura = pyautogui.size()
    MOUSE_MIN_H = largura/40
    MOUSE_MIN_V = altura/40
    pyautogui.FAILSAFE = False
    print(largura, altura)
    # centraliza
    pyautogui.moveTo(largura/2, altura/2, duration=0.5,
                     tween=pyautogui.easeOutQuad)
    ser = serial.Serial('COM3', 115200)
    while(not(keyboard.is_pressed('s'))):
        bruto = str(ser.readline())
        dist = int(re.sub("\D", "", bruto))
        print(dist)
        if (dist < 5 or keyboard.is_pressed("up arrow")):
            pyautogui.move(0, -MOUSE_MIN_V, MOUSE_TIME)


def serial_teste():
    ser = serial.Serial('COM3', 115200)
    '''

    while(True):
        bruto=str(ser.readline())
        char=re.sub("[a-z]+", "", bruto)
        char=re.sub("\\\\", "", char)
        char=re.sub("'", "", char)
        print(char)
        #print(int(char))
    '''
    while (True):
        print(get_distances(ser))


def get_distances(ser):

    getA, getB, getC, getD, getE = False, False, False, False, False
    dist = []
    while(not(getA and getB and getC and getD and getE)):
        bruto = str(ser.readline())
        char = re.sub("[a-z]+", "", bruto)
        char = re.sub("\\\\", "", char)
        char = re.sub("'", "", char)
        if(char == "A"):
            bruto = str(ser.readline())
            dist.append(["A", int(re.sub("\D", "", bruto))])
            getA = True
        elif(char == "B"):
            bruto = str(ser.readline())
            dist.append(["B", int(re.sub("\D", "", bruto))])
            getB = True
        elif(char == "C"):
            bruto = str(ser.readline())
            dist.append(["C", int(re.sub("\D", "", bruto))])
            getC = True
        elif(char == "D"):
            bruto = str(ser.readline())
            dist.append(["D", int(re.sub("\D", "", bruto))])
            getD = True
        elif(char == "E"):
            bruto = str(ser.readline())
            dist.append(["E", int(re.sub("\D", "", bruto))])
            getE = True

    i = 1
    menor = dist[0]
    while(i < 4):
        if((dist[i][1] != 0 and dist[i][1] < menor[1]) or (menor[1] == 0 and dist[i][1] != 0)):
            menor = dist[i]
        i = i+1
    # print(menor[1])
    if(menor[1] <= 10):
        return menor[0]
    return False


# Request_Blink()
# mouse()
serial_teste()
# mouse_sensor()
