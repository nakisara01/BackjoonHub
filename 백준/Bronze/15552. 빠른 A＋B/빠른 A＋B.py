import sys
T=int(input())
S=[]
for i in range(T):
    A, B= map(int, sys.stdin.readline().split())
    S.append(A+B)
print(*S, sep='\n')