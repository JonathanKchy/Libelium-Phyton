import serial
import time

archivo =open('E:\\classs\\C_C++\\holaq.txt','w')
serialArduino=serial.Serial("COM7",115200)
time.sleep(1)

while True:
    cad=serialArduino.readline().decode('ascii')
    archivo.write(cad)
    print(cad)

    