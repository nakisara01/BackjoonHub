def bfs(graph, start_x, start_y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((start_x, start_y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

    return graph[len(graph) - 1][len(graph[0]) - 1]


import sys
from collections import deque

input = sys.stdin.readline
graph = []

N, M = map(int,input().split())

for _ in range(N):
    tmp = input().strip()
    graph.append(list(map(int, tmp)))

result = bfs(graph, 0, 0)
print(result)