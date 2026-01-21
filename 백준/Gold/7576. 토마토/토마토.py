import sys
input = sys.stdin.readline

from collections import deque

M, N = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

q = deque()

for y in range(N):
    for x in range(M):
        if graph[y][x] == 1:
            q.append((y, x))

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

while q:
    y, x = q.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < N and 0 <= nx < M:
            if graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                q.append((ny, nx))

ans = 0

for y in range(N):
    for x in range(M):
        if graph[y][x] == 0:
            print(-1)
            sys.exit(0)
        elif graph[y][x] > ans:
            ans = graph[y][x]

print(ans - 1)