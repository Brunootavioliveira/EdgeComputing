import serial
import time 

porta = 'COM5'
velocidade = 9600
ser = serial.Serial(porta, velocidade, timeout=1)

time.sleep(2)

while True:
    letra = input("Digite A para ligar o led1, B para desligar o led1, C para ligar o led2 e D para ligar o led2")
    ser.write(letra.encode())

    time.sleep(0.2)

    