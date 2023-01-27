import sys

N=int(sys.stdin.readline())
cnt=1
S=1 #벌집의 갯수

while N>S:
    S+=6*cnt
    cnt+=1
print(cnt)