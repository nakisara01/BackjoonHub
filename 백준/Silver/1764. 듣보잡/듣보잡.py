import sys
input = sys.stdin.readline

N, M = map(int, input().split())

hear = set()
for _ in range(N):
    hear.add(input().rstrip())

see = []
for _ in range(M):
    see.append(input().rstrip())

empty = []

for people in see:
    if people in hear:
        empty.append(people)

empty.sort()

print(len(empty))
for i in empty:
    print(i)