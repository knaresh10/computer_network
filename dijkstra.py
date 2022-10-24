MAX_VALUE = int(1e7)
def minDistance(n, distance , visited):
    min = MAX_VALUE
    min_ind = 0
    for node in range(n):
        if distance[node] < min and visited[node] == False:
            min = distance[node]
            min_ind = node
    
    return min_ind


n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

src = int(input())


distance = [MAX_VALUE] * n
distance[src - 1] = 0
visited = [False] * n 


for i in range(n):
    node = minDistance(n, distance, visited)

    visited[node] = True 

    for v in range(n):
        if(graph[node][v] > 0 and visited[v] == False and distance[v] > distance[node] + graph[node][v]):
            distance[v] = distance[node] + graph[node][v]
        
for v in range(n):
    print(v + 1, distance[v])

