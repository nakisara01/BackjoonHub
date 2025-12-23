import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
chk = [[False] * N for _ in range(N)]

def dfs(r, c):
    if r < 0 or r >= N or c < 0 or c >= N:
        return False
    
    if chk[r][c]:
        return False
    
    chk[r][c] = True

    if graph[r][c] == -1:
        return True
    
    k = graph[r][c]

    return dfs(r + k , c) or dfs(r, c + k)

print("HaruHaru" if dfs(0,0) else "Hing")