import sys
input = sys.stdin.readline

from collections import deque

N = int(input())

s = deque()
res = []

for i in range(N):
    tmp = list(map(str, input().split()))

    if tmp[0] == "empty":
        if len(s) == 0:
            res.append(1)
        else:
            res.append(0)
    elif tmp[0] == "top":
        if len(s) == 0:
            res.append(-1)
        else:
            res.append(int(s[-1]))
    elif tmp[0] == "push":
        s.append(tmp[1])
    elif tmp[0] == "pop":
        if len(s) == 0:
            res.append(-1)
        else:
            t = int(s.pop())
            res.append(t)
    elif tmp[0] == "size":
        res.append(len(s))
    else:
        print("err")

for i in res:
    print(i)