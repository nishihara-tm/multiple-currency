import socket

PORT = 5555
#HOST = "192.168.3.3"
#HOST = "127.0.0.1"
HOST = "0.0.0.0"
BUFFER_SIZE = 16

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  data = input("Please input > ")
  s.send(data.encode())
  print(s.recv(BUFFER_SIZE).decode())