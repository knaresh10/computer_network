import socket
import time
s=socket.socket()
s.connect(("localhost", 8020))
while 1:
    msg=s.recv(1).decode()
    print("Received --> ",int(msg))
    s.send(str(msg).encode())
    time.sleep(1)

