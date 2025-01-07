import sys
input = sys.stdin.readline

vertex = int(input())
find_1, find_2 = map(int,input().split())
line = int(input())

graph = [[]for _ in range(vertex+1)]
visited = [False] * (vertex+1)

for _ in range(line):
    x,y = map(int, input().split())
    if x not in graph[y]:
        graph[y].append(x)
    if y not in graph[x]:
        graph[x].append(y)
        
found = False
distance = 0 
    
def DFS(start, depth):
    global found, distance
    visited[start] = True

    if start == find_2:
        found = True
        distance = depth
        return

    for i in graph[start]:
        if not visited[i]:
            DFS(i, depth + 1)
            if found:
                return

DFS(find_1, 0)

if found:
    print(distance)
else:
    print(-1)