import sys
input = sys.stdin.readline

N = int(input())
S = set(map(int, input().rstrip().split()))
M = int(input())
deck = list(map(int, input().rstrip().split()))

for i in range(M):
    if deck[i-1] in S:
        deck[i-1] = 1
    else:
        deck[i-1] = 0

print(*deck)