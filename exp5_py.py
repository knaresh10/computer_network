# // IMPLEMENTATION OF DISTANCE VECTOR:

INFINITY = 10000
adj = path = se = length = [[0]*50]*50
s = t = c = 0

n = int(input("Enter No of Routers: "))
print("Enter Adjacency Matrix")
for i in range(n):
    adj[i] = list(map(int, input().split()))

# Initialization Part
for i in range(n):
    for j in range(n):
        if adj[i][j] == 0 and i != j:
            length[i][j] = INFINITY
            path[i][j] = 0
        else:
            length[i][j] = adj[i][j]
            path[i][j] = j

        if (i == j):
            path[i][j] = 131


# Iteration Part
t = 1
while t:
    c = 0
    for s in range(n):
        for j in range(n):
            if adj[s][j]:
                for i in range(n):
                    if ((length[s][j] + length[j][i]) < length[s][i]):
                        length[s][i] = length[s][j] + length[j][i]
                        path[s][i] = j

    for s in range(n):
        for i in range(n):
            if length[s][i] == INFINITY:
                c += 1
    if c == 0:
        t = 0
    else:
        t = 1

print("\nRouting table\n\n")
for i in range(65, 66+n):
    print(" ", chr(i), " ", end=' ')
print("\n----------------------------------------------------\n")
for i in range(n):
    print(" l  p ", end=' ')

print("\n---------- ----- ------ ------ ------ ------ -------\n")
for i in range(n):
    print(chr(i+65), end=' ')
    for s in range(n):
        print(length[s][i], chr(path[s][i]+65), " |", end=' ')
    print()
