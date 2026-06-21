# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 11:03:06 2026

@author: akcay
"""

import serial
import time
arduino=serial.Serial("COM3",9600)
print("Arduino bekleniyor")
time.sleep(3)
print(arduino)
print("Bağlantı basasrıyla  kuruldu")
while True:
    veri=input("""lutfen LED açmak için 'a' harfine,sondurmek için 'b' basiniz(çikmak için
               'z' harfi):""")
    if(veri=="a"):
        arduino.write(b'a')
    elif(veri=="b"):
        arduino.write(b'b')
    elif(veri=="z"):
        print("güle güle")
        break