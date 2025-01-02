import socket

s = socket.socket()

print("Server created")
s.bind(("localhost", 999))
s.listen(3)
print("Waiting for connection")

conn = True
while conn:
    c, addr = s.accept()
    print(addr)
    receivedMsg = c.recv(1024).decode()
    print("Client:", receivedMsg)
    if receivedMsg == "exit":
        conn = False
        break
    msg = input("Enter your message: ")
    c.send(bytes(msg, 'UTF-8'))

c.close()
s.close()