import sys
input = sys.stdin.readline

cow = {}
cnt = 0

for i in range(int(input())):
    N, K = map(int, input().split())

    if N in cow:
        if cow[N] == K:
            pass
        else:
            cnt += 1
            cow[N] = K
    else:
        cow[N] = K

print(cnt)