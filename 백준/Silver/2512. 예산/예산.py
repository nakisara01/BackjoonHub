import sys
input = sys.stdin.readline

N = int(input())
money = list(map(int, input().split()))
limit = int(input())

money.sort()

def check(cap):
    total = 0

    for i in range(N):
        total += min(money[i], cap)

    return total <= limit

res = 0

start = 0
end = money[-1]

while start <= end:
    mid = (start + end) // 2

    if check(mid):
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)