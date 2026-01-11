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

def DFS(graph, start, visited):
    visited[start] = True

    for next in graph[start]:
        if not visited[next]:
            DFS(graph, next, chk)

DFS(graph, 1, chk)

print(sum(chk) - 1)