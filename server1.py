import socket
import time
import random
s = socket.socket()
s.bind(("localhost",8020))
s.listen(5)
c, adr =s.accept()
print("connection to " + str(adr) + " established")
n = int(input("Enter number of frames: "))
N = int(input("Enter window size: "))
start = 0
end = 0
frame = 0
for i in range(N):
    print("sending --> ", frame)
    c.send(str(frame).encode())
    frame += 1
    end += 1
    time.sleep(1)

timer = 5

while start < n :
    msg = c.recv(1).decode()
    msg = int(msg)

    if(msg != start): 
        continue

    t = random.randint(1, 7)
    if(timer > t):
        print("ack --> ",start)
        if(frame < n):
            print("sending -->",frame)
            c.send(str(frame).encode())
            frame += 1
            end += 1
        start += 1
        time.sleep(2)
    else:
        print("Timeout")
        frame = start
        for i in range(start, end):
            print("sending again --> ",frame)
            c.send(str(frame).encode())
            frame += 1
            time.sleep(1)