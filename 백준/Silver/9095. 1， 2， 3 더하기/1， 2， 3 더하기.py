import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
max_n = max(arr)

dp = [0] * (max_n + 1)

if max_n >= 1:
    dp[1] = 1
if max_n >= 2:
    dp[2] = 2
if max_n >= 3:
    dp[3] = 4
 
for i in range(4, max_n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for i in arr:
    print(dp[i])