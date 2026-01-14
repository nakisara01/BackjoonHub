import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for i in range(1, M + 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

cnt = 0

def DFS(start):
    visited[start] = True
    
    for i in graph[start]:
        if not visited[i]:
            DFS(i)

for i in range(1, N + 1):
    if not visited[i]:
        cnt += 1
        DFS(i)

print(cnt)