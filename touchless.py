import pyautogui # Controla o Mouse e teclado
import keyboard # Pega os dados do Teclado instantaneamente
import requests # faz requests http
from socket import gethostbyname #requisição DNS Automatica
import serial # comunicação serial com a Wemos 
import re #regx

def main():

    auth=Request_Blink()
    if(auth==True):
        print("Usuário autenticado")
        mouse_sensor()
    else:
        print("Erro de autenticação")


def Request_Blink():

    auth_token = "lh-Y66OTh4k-_laDnmFeRIOBKyHE5z5O"
    blynk_server = gethostbyname("blynk-cloud.com") # pega o ip automaticamente
    pinled = 'V77'
    pin = 'V77'
    
    #liga o led
    requests.get('http://'+blynk_server+'/'+auth_token+'/update/'+pinled+'?value=U')
    r = requests.get('http://'+blynk_server+'/'+auth_token+'/get/'+pin)
    bruto=str(r.text)
    lista=re.sub("\D", "", bruto)
    char=lista[len(lista)-1]
    print(char)
    if(char=="0"):
        return(True)
    return(False)

def mouse_sensor():
    fp = open('log.txt', 'a')
    MOUSE_TIME=0.00
    largura, altura= pyautogui.size()
    MOUSE_MIN_H=largura/40
    MOUSE_MIN_V=altura/40
    pyautogui.FAILSAFE = False
    print(largura, altura)
    #centraliza
    pyautogui.moveTo(largura/2, altura/2, duration = 0.5, tween = pyautogui.easeOutQuad)
    ser = serial.Serial('COM3',115200)
    while(not(keyboard.is_pressed('s'))):
        command=get_distances(ser)
        if (command=="A" or keyboard.is_pressed("up arrow") ):
            pyautogui.move(0, -MOUSE_MIN_V, MOUSE_TIME)
        if (command=="B" or keyboard.is_pressed("down arrow") ):
            pyautogui.move(0, MOUSE_MIN_V, MOUSE_TIME)
        if (command=="C" or keyboard.is_pressed("left arrow") ):
            pyautogui.move(-MOUSE_MIN_H, 0, MOUSE_TIME) 
        if (command=="D" or keyboard.is_pressed("down arrow") ):
            pyautogui.move(MOUSE_MIN_H, 0, MOUSE_TIME) 
        if (command=="E" or keyboard.is_pressed("0") ):
            pyautogui.click()
        if(command!=False):
            fp.write(command+" \n")
    fp.close
def get_distances(ser):
    
    getA,getB,getC,getD,getE=False,False,False,False,False
    dist=[]
    while(not(getA and getB and getC and getD and getE)):
        bruto=str(ser.readline())
        char=re.sub("[a-z]+", "", bruto)
        char=re.sub("\\\\", "", char)
        char=re.sub("'", "", char)
        if(char=="A"):
            bruto=str(ser.readline())
            dist.append(["A",int(re.sub("\D", "", bruto))])
            getA=True
        elif(char=="B"):
            bruto=str(ser.readline())
            dist.append(["B",int(re.sub("\D", "", bruto))])
            getB=True
        elif(char=="C"):
            bruto=str(ser.readline())
            dist.append(["C",int(re.sub("\D", "", bruto))])
            getC=True
        elif(char=="D"):
            bruto=str(ser.readline())
            dist.append(["D",int(re.sub("\D", "", bruto))])
            getD=True
        elif(char=="E"):
            bruto=str(ser.readline())
            dist.append(["E",int(re.sub("\D", "", bruto))])
            getE=True

    i=1
    
    menor=dist[0]
    while(i<4):
        if((dist[i][1]!=0 and dist[i][1]<menor[1]) or (menor[1]==0 and dist[i][1]!=0)):
            menor=dist[i]
        i=i+1
    #print(menor[1])
    if(menor[1]<=10):
        return menor[0]
    return False

    
    
main()