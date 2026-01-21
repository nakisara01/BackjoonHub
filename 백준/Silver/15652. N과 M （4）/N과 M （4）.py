import sys
input = sys.stdin.readline
write = sys.stdout.write
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

arr = []

def dfs(depth, start):
    if depth == M:
        write(' '.join(arr) + '\n')
        return

    for i in range(start, N + 1):
        arr.append(str(i))
        dfs(depth + 1, i)
        arr.pop()

dfs(0, 1)