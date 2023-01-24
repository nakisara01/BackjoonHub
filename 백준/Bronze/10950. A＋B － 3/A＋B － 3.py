T=int(input())
S=[]

for i in range(T):
    A, B= map(int, input().split())
    S.append(A+B)

print(*S, sep='\n')