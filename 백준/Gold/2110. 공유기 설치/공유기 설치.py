import sys
input = sys.stdin.readline

N, C = map(int, input().split())
houses = []

for i in range(N):
    houses.append(int(input()))

houses.sort()

def check(d):
    cnt = 1
    last = houses[0]
    for i in range(1, N):
        if last + d <= houses[i]:
            cnt += 1
            last = houses[i]
    return cnt >= C

start, end = 0, houses[-1] - houses[0]
ans = 0

while start <= end:
    mid = (start + end) // 2

    if check(mid):
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)