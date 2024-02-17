import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            print("Mensaje recibido:", message.decode())
            broadcast(message, client_socket)
        except Exception as e:
            print("Error:", e)
            break

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)

my_socket = socket.socket()
my_socket.bind(('localhost', 8000))

my_socket.listen(5)

print("Esperando conexiones...")

clients = []

while True:
    client_socket, addr = my_socket.accept()
    print("Cliente conectado desde:", addr)
    clients.append(client_socket)

    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
