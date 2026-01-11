import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))
x = int(input())

li.sort()

start = 0
end = len(li) - 1
cnt = 0

while(start < end):
    s = li[start] + li[end]

    if s == x:
        cnt += 1
        start += 1
        end -= 1
    elif s < x:
        start += 1
    else:
        end -= 1

print(cnt)