A, B=map(int, input().split())
C= int(input())

if B+C>=59:
    M=(B+C)//60
    D=(B+C)%60
    B=D
    A=A+M

    if A>23:
        A=A-24
else:
    B=B+C

print(A, B)