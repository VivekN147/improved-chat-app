import time
import socket
import sys

print("Welcome to Python Chat Version 2.0")
print("")
print("Initializing...")
time.sleep(1)

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))
print("")
print(host)
print("")
name = input(str("Please Enter Your Username : "))
s.listen(1)
print("")
print("Waiting for any incoming connections...")
print("")
conn, addr = s.accept()
print("Received connection.")

## connection done. ##

s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "Has connected to the Chat Room.")
print("")
conn.send(name.encode())

## message loop ##

while 1:
    message = input(str("Please Enter Your Message :"))
    conn.send(message.encode())
    print("Sent.")
    message = conn.recv(1024)
    message = message.decode()
    print("")
    print(name, " : ", message)
    print("")