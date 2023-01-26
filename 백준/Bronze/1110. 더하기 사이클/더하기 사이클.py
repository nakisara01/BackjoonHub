import sys

N=int(sys.stdin.readline())
A=N
cnt=0
while 1:
        A=(A%10)*10+(((A//10)+(A%10))%10)
        cnt+=1
        if A==N:
            print(cnt)
            break