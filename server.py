import socket

my_socket = socket.socket()
my_socket.bind(('localhost',8000))

my_socket.listen(5)

on = True

while on:
    connection, addr = my_socket.accept()
    print("Nueva conexion")
    print(addr)

    petition = connection.recv(1024)
    print(petition)

    connection.send(b"Hola desde el server")
    connection.close()