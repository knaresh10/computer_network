import socket
import time
import random
s = socket.socket()
s.bind(("localhost",8020))
s.listen(5)
c, adr =s.accept()
print("address of the client ",str(adr))
n = int(input("Enter number of frames: "))
N = int(input("Enter window size: "))
windowStart = 0
windowEnd = 0
frame = 0
for i in range(N):
    print("Frame sent --> ", frame)
    c.send(str(frame).encode())
    frame += 1
    windowEnd += 1
    time.sleep(1)

timer = 5

while windowStart < n :
    msg = c.recv(1).decode()
    msg = int(msg)

    if(msg != windowStart): 
        continue

    t = random.randint(1, 7)
    if(timer > t):
        print("acknowledgement received for ",windowStart)
        if(frame < n):
            print("frame sent -->",frame)
            c.send(str(frame).encode())
            frame += 1
            windowEnd += 1
        windowStart += 1
        time.sleep(2)
    else:
        print("acknowledgement not received for ",windowStart)
        frame = windowStart
        for i in range(windowStart, windowEnd):
            print("Frame sent --> ",frame)
            c.send(str(frame).encode())
            frame += 1
            time.sleep(1)