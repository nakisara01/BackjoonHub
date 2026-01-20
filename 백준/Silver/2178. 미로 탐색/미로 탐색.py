import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())

graph = [list(map(int, input().strip())) for _ in range(N)]
dist = [[-1 for _ in range(M)] for _ in range(N)]

ny = [1, -1, 0, 0]
nx = [0, 0, 1, -1]

def bfs():
    q = deque()
    q.append((0,0))
    dist[0][0] = 1

    while q:
        y, x = q.popleft()

        for i in range(4):
            dy = y + ny[i]
            dx = x + nx[i]

            if 0 <= dy < N and 0 <= dx < M:
                if graph[dy][dx] == 1 and dist[dy][dx] == -1:
                    dist[dy][dx] = dist[y][x] + 1
                    q.append((dy, dx))

bfs()

print(dist[N - 1][M - 1])