import sys
input = sys.stdin.readline

N = int(input())
line = [list(map(int, input().split())) for _ in range(N)]
lis = []
dp = [1] * N

line.sort()

for i in range(N):
    lis.append(line[i][1])

for i in range(N):
    for j in range(i):
        if lis[j] < lis[i]:
            dp[i] = max(dp[j] + 1, dp[i])
            
print(N - max(dp))