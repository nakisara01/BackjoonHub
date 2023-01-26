X=True

while X:
    A, B=map(int, input().split())
    if A==B and A==0:
        break
    else:
        print(A+B)