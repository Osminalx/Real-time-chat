import socket
import threading

class Client:
    def __init__(self):
        print("Conectando al servidor...\n")
        self.my_socket = socket.socket()
        self.my_socket.connect(('localhost', 8000))
        print("Conectado al Servidor!\n")

    def send(self):
        message = input("Yo:")
        self.my_socket.send(message.encode())

    def recieve(self):
        while True:
            try:
                message = self.my_socket.recv(1024)
                if not message:
                    break
                print("Servidor:", message.decode())
            except Exception as e:
                print("Error:", e)
                break

    def close_socket(self):
        self.my_socket.close()
        print("Socket cerrado.\n")

def main():
    client = Client()
    receive_thread = threading.Thread(target=client.recieve)
    receive_thread.start()

    while True:
        client.send()

    cliente.close_socket()

if __name__ == "__main__":
    main()

