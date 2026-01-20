import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

dist = [[[-1, -1] for _ in range(M)] for _ in range(N)]

ex = [0, 0, 1, -1]
ey = [1, -1 ,0, 0]

def bfs():
    q = deque()
    q.append((0, 0, 0))
    dist[0][0][0] = 1

    while q:
        y, x, broke = q.popleft()

        for i in range(4):
            ny = y + ey[i]
            nx = x + ex[i]

            if not (0 <= ny < N and 0 <= nx < M):
                continue

            if graph[ny][nx] == 0:
                if dist[ny][nx][broke] == -1:
                    dist[ny][nx][broke] = dist[y][x][broke] + 1
                    q.append((ny, nx, broke))
            
            else:
                if broke == 0 and dist[ny][nx][1] == -1:
                    dist[ny][nx][1] = dist[y][x][0] + 1
                    q.append((ny, nx, 1))


bfs()

mini = dist[N - 1][M - 1][0]
mini_broken = dist[N - 1][M - 1][1]

if mini == mini_broken == -1:
    print(-1)
elif mini == -1:
    print(mini_broken)
elif mini_broken == -1:
    print(mini)
else:
    print(min(mini, mini_broken))