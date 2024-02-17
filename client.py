import socket

my_socket = socket.socket()
my_socket.connect(('localhost',8000))

my_socket.send(b"Hola desde el cliente")
res = my_socket.recv(1024)

print(res)
my_socket.close()