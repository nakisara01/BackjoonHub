import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rice_cake = list(map(int, input().split()))

start = 0
end = max(rice_cake)

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2

    for piece in rice_cake:
        if piece > mid:
            total += piece - mid
    
    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)