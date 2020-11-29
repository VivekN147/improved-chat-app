import time
import socket
import sys

print("Welcome to Python Chat Version 2.0")
print("")
print("Initializing...")
time.sleep(1)

s = socket.socket()
print("")
host = input(str("Please enter the server address : "))
print("")
name = input(str("Please Enter Your Name : "))
port = 8080
print("")
print("Trying to connect to", host, " At Port ", port)
print("")
time.sleep(1)
s.connect((host,port))
print("Connected.")

## connection done. ##

s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print("")
print(s_name, "Has joined the Chat Room")

## message loop ##

while 1:
    message = s.recv(1024)
    message = message.decode()
    print("")
    print(name, " : ", message)
    print("")
    message = input(str("Please Enter Your Message : "))
    print("")
    s.send(message.encode())
    print("Sent.")