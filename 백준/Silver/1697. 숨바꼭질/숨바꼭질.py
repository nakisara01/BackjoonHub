import sys
input = sys.stdin.readline

from collections import deque

N, K = map(int, input().split())
dist = [-1] * 100001

def operations(x, i):
    if i == 0:
        x += 1
        return x
    elif i == 1:
        x -=1
        return x
    else:
        x = x * 2
        return x

if N == K:
    print(0)
    exit()

def bfs(now, goal):
    dist[now] = 0
    q = deque()
    q.append(now)
    while q:
        x = q.popleft()
        for i in range(3):
            tmp = operations(x, i)
            if tmp < 0 or tmp > 100000: 
                continue
            if tmp == goal:
                dist[tmp] = dist[x] + 1
                return dist[goal]
            elif dist[tmp] == -1:
                q.append(tmp)
                dist[tmp] = dist[x] + 1

print(bfs(N, K))