import sys
input = sys.stdin.readline

from collections import deque

F, S, G, U, D = map(int, input().split())
dist = [-1] * (F + 1)

def bfs():
    if S == G:
        return 0
    q = deque()
    q.append(S)
    dist[S] = 0
    while q:
        now = q.popleft()
        for i in (now + U, now - D):
            if 0 < i <= F and dist[i] == -1:
                dist[i] = dist[now] + 1
                if i == G:
                    return dist[i]
                q.append(i)
    return -1

rs = bfs()

print(rs if rs != -1 else "use the stairs")