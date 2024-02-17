import socket
import threading

def receive_messages():
    while True:
        try:
            message = my_socket.recv(1024)
            if not message:
                break
            print("Servidor:", message.decode())
        except Exception as e:
            print("Error:", e)
            break

my_socket = socket.socket()
my_socket.connect(('localhost', 8000))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()


while True:
    message = input("Yo:")
    my_socket.send(message.encode())

my_socket.close()
