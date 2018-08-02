import socket
import sys
import time



s = socket.socket()
host = '127.0.0.1'
print(" sunucu anabilgisayara bağlanicak : ", host)
port =3000
s.bind((host, port))
print("")
print(" sunucu başarıyla başlandı")
print("")
print("sunucuya bağlantı bekleniyor")
print("")
s.listen(1)
baglanti,adres = s.accept()
print(adres, " sunucuya bağlandı ve çevrimiçi")
print("")
while 1:
    mesaj = input(str(">> "))
    mesaj = mesaj.encode()
    baglanti.send(mesaj)
    print("mesaj gönderiliyor.")
    print("")
    gelenMesaj = baglanti.recv(1024)
    gelenMesaj = gelenMesaj.decode()
    print(" Kullanıcı2 : ", gelenMesaj)
    print("")

