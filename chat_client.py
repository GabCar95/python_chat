import socket

#Define constants to be used
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))


#Send/receive msg

while True:
    message = client_socket.recv(BYTESIZE).decode(ENCODER)

    #Quit if connected server wants to quite else keep sending msg
    if message == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("\nEnding the chat... goodbye!")
        break
    else:
        print(f"\n{message}")
        message = input("Message: ")
        client_socket.send(message.encode(ENCODER))

#close the client socket
client_socket.close()