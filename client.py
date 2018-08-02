import socket
import sys
import time

s = socket.socket()
host = input("bilgisayar adini girin ")
port = 3000
s.connect((host, port))
print(" servera bağlanıldı")
while 1:
    gelenMesaj = s.recv(1024)
    gelenMesaj = gelenMesaj.decode()
    print(" Server : ", gelenMesaj)
    print("")
    mesaj = input(str(">> "))
    mesaj = mesaj.encode()
    s.send(mesaj)

    print("mesaj gönderiliyor.")
    print("")
