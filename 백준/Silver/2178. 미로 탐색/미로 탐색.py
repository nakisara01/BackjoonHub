import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
dist = [[-1] * M for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs():
    q = deque()
    q.append((0, 0))
    dist[0][0] = 1

    while q:
        ey, ex = q.popleft()
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]

            if 0 <= ny < N and 0 <= nx < M:
                if ny + 1 == N and nx + 1 == M:
                    dist[ny][nx] = dist[ey][ex] + 1
                    return dist[ny][nx]
                elif graph[ny][nx] == 1 and dist[ny][nx] == -1:
                    dist[ny][nx] = dist[ey][ex] + 1
                    q.append((ny, nx))

print(bfs())