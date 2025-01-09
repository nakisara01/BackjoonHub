import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y, height):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if graph[x][y] > height and not visited[x][y]:
        visited[x][y] = True
        dfs(x-1, y, height)
        dfs(x+1, y, height)
        dfs(x, y-1, height)
        dfs(x, y+1, height)
        return True
    return False

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

max_height = max(map(max, graph))
result = 0

for height in range(max_height + 1):
    visited = [[False] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if dfs(i, j, height):
                count += 1
    result = max(result, count)

print(result)