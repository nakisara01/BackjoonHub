import sys
input = sys.stdin.readline

vertex = int(input())
line = int(input())

visited = [False] * (vertex+1)
graph = [[] for _ in range(vertex+1)]

for _ in range(line):
    x,y = map(int, input().split())
    if x not in graph[y]:
        graph[y].append(x)
    if y not in graph[x]:
        graph[x].append(y)

def DFS(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            DFS(i)

DFS(1)
cnt = 0
for i in visited:
    if i == True:
        cnt+=1
print(cnt-1)