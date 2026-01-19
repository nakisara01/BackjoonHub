import sys
input = sys.stdin.readline

from collections import deque

N, K = map(int, input().split())
dist = [-1] * 100001

def bfs():
    q = deque()
    q.append(N)
    dist[N] = 0
    
    if N == K:
        return 0

    while q:
        x = q.popleft()

        for next in [x + 1, x - 1, x * 2]:
            if not 0 <= next <= 100000: continue

            if next == K:
                return dist[x] + 1
            elif next != K and dist[next] == -1:
                dist[next] = dist[x] + 1
                q.append(next)

print(bfs())