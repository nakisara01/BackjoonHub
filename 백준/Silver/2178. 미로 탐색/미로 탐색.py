from collections import deque

import sys
input = sys.stdin.readline

n, m = map(int, input(). split())
map = [list(map(int, input().strip())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(y, x):
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if map[ny][nx] == 1:
                    map[ny][nx] = map[y][x] + 1
                    q.append((ny, nx))
    return map[n-1][m-1]

print(bfs(0,0))