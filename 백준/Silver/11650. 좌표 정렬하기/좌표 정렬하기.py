import sys
input = sys.stdin.readline

N = int(input())
axis = [list(map(int,input().split())) for _ in range(N)]
axis.sort()

for i in axis:
    print(i[0], i[1])