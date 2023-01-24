A, B, C=map(int, input().split())
S=0

if A==B and B==C:
    S=10000+A*1000
elif (A==B and B!=C):
    S=1000+A*100
elif (B==C and A!=B):
    S=1000+B*100
elif (A==C and B!=C):
    S=1000+A*100
else:
    max=max(A,B,C)
    S=max*100

print(S)