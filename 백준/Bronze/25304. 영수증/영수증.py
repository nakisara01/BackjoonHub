X=int(input())
N=int(input())
Y=0

for i in range(N):
    a, b=map(int, input().split())
    S=a*b
    Y=Y+S
if X==Y:
    print("Yes")
else:
    print("No")