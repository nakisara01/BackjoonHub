import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

res = [0]

dx = [0, 0, -1, 1]
dy = [1, -1 , 0, 0]

def bfs(y, x):
    q = deque()
    q.append((y,x))
    visited[y][x] = True
    cnt = 1

    while q:
        tmpy, tmpx = q.popleft()

        for i in range(4):
            ny = tmpy + dy[i]
            nx = tmpx + dx[i]

            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == 1 and visited[ny][nx] == False:
                    q.append((ny,nx))
                    visited[ny][nx] = True
                    cnt += 1
    return cnt

for j in range(N):
    for i in range(M):
        if visited[j][i] == False and graph[j][i] == 1:
            res.append(bfs(j,i))

if len(res) == 1:
    print(0)
    print(0)
else:
    print(len(res) - 1)
    print(max(res))