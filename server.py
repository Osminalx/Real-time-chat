import socket
import threading

class ChatManager:
    def __init__(self):
        self.clients = []

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

class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('localhost', 8000))
        self.server.listen(5)
        print("Esperando conexiones...")

    def start(self):
        while True:
            client_socket, addr = self.server.accept()
            print("Cliente conectado desde:", addr)
            chat_manager.clients.append(client_socket)

            client_handler = threading.Thread(target=chat_manager.handle_client, args=(client_socket,))
            client_handler.start()

if __name__ == "__main__":
    chat_manager = ChatManager()
    server = Server()
    server.start()
