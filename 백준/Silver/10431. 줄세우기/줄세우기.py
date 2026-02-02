import sys
input = sys.stdin.readline

for i in range(int(input())):
    li = list(map(int, input().split()))
    ans = 0

    for j in range(2, 21):
        for k in range(j, 1, -1):
            if li[k] < li[k-1]:
                li[k], li[k-1] = li[k-1], li[k]
                ans += 1
    print(li[0], ans)