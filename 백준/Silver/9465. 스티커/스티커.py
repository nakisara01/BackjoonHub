import sys
input = sys.stdin.readline

T = int(input())

res = []

for _ in range(T):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(2)]

    dp = [[0, 0, 0] for _ in range(n)]

    dp[0][0] = 0
    dp[0][1] = arr[0][0]
    dp[0][2] = arr[1][0]

    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + arr[0][i]
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + arr[1][i]
    
    res.append(max(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]))

print(*res, sep = '\n')