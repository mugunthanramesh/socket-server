import socket
import sys
import time
message=''
s=socket.socket()
host=input("Enter hostname:")
port=8080
s.connect((host,port))
print("Connected to server")
while(message!='exit'):
    incoming = s.recv(1024)
    incoming = incoming.decode()
    print("Server:", incoming)
    message = input("Message:")
    message = message.encode()
    s.send(message)
    print("Message Sent!")