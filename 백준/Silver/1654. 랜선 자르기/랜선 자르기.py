import sys
input = sys.stdin.readline

K, N = map(int, input().split())
line = []

for _ in range(K):
    tmp = int(input())
    line.append(tmp)

start = 1
end = max(line)

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2

    for i in line:
        if i >= mid:
            total += i // mid
    if total < N:
        end = mid -1
    else:
        result = mid
        start = mid + 1

print(result)