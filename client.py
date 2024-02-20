import socket
import threading

class Cliente:
    def __init__(self):
        print("Conectando al servidor...\n")
        self.my_socket = socket.socket()
        self.my_socket.connect(('localhost', 8000))
        print("Conectado al Servidor!\n")

    def enviar(self):
        message = input("Yo:")
        self.my_socket.send(message.encode())

    def recibir(self):
        while True:
            try:
                message = self.my_socket.recv(1024)
                if not message:
                    break
                print("Servidor:", message.decode())
            except Exception as e:
                print("Error:", e)
                break

    def cerrar_socket(self):
        self.my_socket.close()
        print("Socket cerrado.\n")

def main():
    cliente = Cliente()
    receive_thread = threading.Thread(target=cliente.recibir)
    receive_thread.start()

    while True:
        cliente.enviar()

    cliente.cerrar_socket()

if __name__ == "__main__":
    main()

