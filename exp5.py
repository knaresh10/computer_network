INFINITE = 10000

n = int(input("Enter number of routers"))
adj = []
for i in range(n):
    adj.append(list(map(int,input().split())))

length = path = [[0]*50] * 50

for i in range(n):
    for j in range(n):
        if adj[i][j] == 0 and i != j:
            length[i][j] = INFINITE
            path[i][j] = 0
        else:
            length[i][j] = adj[i][j]
            path[i][j] = j 
        if i == j:
            path[i][j] = 131
    
t = 1
while t:
    c = 0 
    for i in range(n):
        for j in range(n):
            if adj[i][j]:
                for k in range(n):
                    if length[i][j] + length[j][k] < length[i][k]:
                        length[i][j] += length[j][k]
                        path[i][k] = j

    for i in range(n):
        for j in range(n):
            if length[i][j] == INFINITE:
                c += 1 
    
    if c == 0:
        t = 0
    else : 
        t = 1 
    

    print("routing table")
    for i in range(n):
        print(i, endl = " ")
    print("---------------------")
    for i in range(n):
        print(" 1 p")

    print("-----------------------")
    for i in range(n):
        print(i)
        for j in range(n):
            print(length[i][j], char(path[i][j] + 65) ,end = " | ")
        print()