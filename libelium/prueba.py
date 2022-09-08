import serial
import time
from datetime import date
from datetime import datetime

archivo =open('E:\\classs\\C_C++\\temperatura.txt','w')
serialArduino=serial.Serial("COM7",115200)
time.sleep(1)
contador=0

while True:
    if contador == 0:
        archivo.write("Captura;Fecha;Hora;Temperatura (Celsius)\n")
        cad=serialArduino.readline().decode('ascii')
    else:
        print(contador)
        now = datetime.now()
        cad=serialArduino.readline().decode('ascii')
        archivo.write(str(contador)+";"+str(now.year)+"/"+str(now.month)+"/"+str(now.day)
        +";"+str(now.hour)+":"+str(now.minute)+":"+str(now.second)+";"+cad)
        print(cad)
    contador=contador+1

    