import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (N + 1)

def dfs(i):
    visited[i] = True

    for nxt in graph[i]:
        if not visited[nxt]:
            dfs(nxt)

cnt = 0

for i in range(1, N + 1):
    if visited[i] == False:
        dfs(i)
        cnt += 1

print(cnt)