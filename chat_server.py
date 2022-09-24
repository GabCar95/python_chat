from pydoc import cli
import socket

#Define constants to be used
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()


#feedback to user
print("Server is running... \n")

client_socket, client_address = server_socket.accept()
client_socket.send("You are connected to server... \n".encode(ENCODER))


#Send/receive msg
while True:
    message = client_socket.recv(BYTESIZE).decode(ENCODER)

    #Quit if client socket wants to quite else display msg
    if message == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("\nEnding the chat... goodbye!")
        break
    else:
        print(f"\n{message}")
        message = input("Message: ")
        client_socket.send(message.encode(ENCODER))

#close server socket
server_socket.close()
