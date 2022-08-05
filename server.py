import socket
import threading

PORT = 5555
#HOST = "192.168.3.3"
#HOST = "127.0.0.1"
HOST = "0.0.0.0"
BUFFER_SIZE = 4

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
  while True:
    sock, address = s.accept()
    try: 
      print("connected: ", address)
      data = sock.recv(BUFFER_SIZE)
      sock.send(data.upper())
    finally:
      sock.close()