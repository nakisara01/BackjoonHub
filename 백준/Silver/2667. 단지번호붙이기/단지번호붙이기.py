import sys
input = sys.stdin.readline

from collections import deque

N = int(input())

graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

cnt = 0
cnt_list = []

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(y, x):
    q = deque()
    q.append((y,x))
    visited[y][x] = True

    rs = 1

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx] == False and graph[ny][nx] == 1:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    rs += 1
    cnt_list.append(rs)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == False:
            bfs(i, j)
            cnt += 1

print(cnt)
cnt_list.sort()
print(*cnt_list, sep = "\n")