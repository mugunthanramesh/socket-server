import socket
import sys
import time
message=''
s=socket.socket()
host=socket.gethostname()
print("Server will start:",host)
port=8080
s.bind((host,port))
print("Server done binding")
print("Server Waiting for connection")
s.listen()
conn,addr=s.accept()
print(addr,"Has connected")
while (message!='exit'):
    message=input("Message:")
    message=message.encode()
    conn.send(message)
    incoming=conn.recv(1024)
    incoming=incoming.decode()
    print("Client:",incoming)
