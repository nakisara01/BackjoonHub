import sys

vertex, line = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(vertex + 1)]
visited = [False] * (vertex + 1)

for _ in range(line):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0

def DFS(graph, start, visited):
    stack = [start]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            stack.extend(graph[node])

for i in range(1, vertex + 1):
    if not visited[i]:
        DFS(graph, i, visited)
        cnt += 1

print(cnt)
