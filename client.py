import socket

conn = True

while conn:
    c = socket.socket()
    c.connect(('localhost', 999))
    msg = input("Enter your message: ")
    c.send(bytes(msg, "UTF-8"))
    receivedMsg = c.recv(1024).decode()
    if msg == "exit":
        conn = False
        break
    print("Server: ", receivedMsg)

c.close()