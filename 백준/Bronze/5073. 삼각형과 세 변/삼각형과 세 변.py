import sys
input = sys.stdin.readline

while 1:
    A, B, C = map(int, input().split())

    if A == B == C == 0:
        break
    elif A + B <= C or B + C <= A or A + C <= B:
        print("Invalid")
    elif A == B == C:
        print("Equilateral")
    elif A == B or B == C or A == C:
        print("Isosceles")
    else:
        print("Scalene")