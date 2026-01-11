import sys
input = sys.stdin.readline

from collections import deque

com = int(input())
graph = [[] for _ in range(com + 1)]
chk = [False] * (com + 1)

for i in range(int(input())):
    n, m = map(int, input().split())
    graph[n].append(m)
    graph[m].append(n)

def BFS(graph, start, visited):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                q.append(next)

BFS(graph, 1, chk)

print(sum(chk) - 1)