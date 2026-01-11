import sys
input = sys.stdin.readline

from collections import deque

N = int(input())

q = deque()
res = []

for i in range(N):
    li = input().split()

    if li[0] == "push":
        q.append(int(li[1]))
    elif li[0] == "pop":
        if len(q) == 0:
            res.append(-1)
        else:
            t = q.popleft()
            res.append(t)
    elif li[0] == "size":
        res.append(len(q))
    elif li[0] == "empty":
        res.append(0 if q else 1)
    elif li[0] == "front":
        if len(q) == 0:
            res.append(-1)
        else:
            res.append(q[0])
    elif li[0] == "back":
        if len(q) == 0:
            res.append(-1)
        else:
            res.append(q[-1])
    else:
        print("err")

for i in res:
    print(i)