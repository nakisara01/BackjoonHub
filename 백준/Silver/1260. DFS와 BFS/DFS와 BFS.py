from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in graph:
    i.sort()
    
dfs_store = []   
bfs_store = []
    
def dfs(graph, start, visited):
    visited[start] = True
    dfs_store.append(start)
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        bfs_store.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(graph, v, visited)
print(*dfs_store)
visited = [False] * (n+1)
bfs(graph, v, visited)
print(*bfs_store)