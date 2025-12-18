from collections import deque

import sys
input = sys.stdin.readline

n = int(input())
map = list(map(int, input().split()))
chk = [False] * n
s = int(input())

def bfs(s):
    cnt = 1
    s -= 1
    q = deque()
    q.append(s)
    chk[s] = True

    while q: 
        x = q.popleft()
        for i in (x + map[x], x - map[x]):
            if 0 <= i < n and not chk[i]:
                chk[i] = True
                q.append(i)
                cnt += 1
    return cnt

print(bfs(s))