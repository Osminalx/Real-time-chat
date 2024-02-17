import socket
import threading

class chatManager:
    def __init__(self) -> None:
        pass

    def _broadcast(self, message, sender_socket):
        for client in self.clients:
            if client != sender_socket:
                try:
                    client.send(message)
                except:
                    self.clients.remove(client)

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024)
                if not message:
                    break
                print("Mensaje recibido:", message.decode())
                self._broadcast(message, client_socket)
            except Exception as e:
                print("Error:", e)
                break


my_socket = socket.socket()
my_socket.bind(('localhost', 8000))

my_socket.listen(5)

print("Esperando conexiones...")

chat_manager = chatManager()
chat_manager.clients = []

while True:
    client_socket, addr = my_socket.accept()
    print("Cliente conectado desde:", addr)
    chat_manager.clients.append(client_socket)

    client_handler = threading.Thread(target=chat_manager.handle_client, args=(client_socket,))
    client_handler.start()
