#!/usr/bin/python3
#ignore this code and use the MultiClient one!!!!!!!!!!
import socket
import pyaudio
import os

os.nice(-20)

# Socket
HOST = '10.10.22.20'
PORT = 5000

# Audio
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as server_socket:
    while True:
        data = stream.read(CHUNK,exception_on_overflow = False)
        server_socket.sendto(data,(HOST,PORT))
