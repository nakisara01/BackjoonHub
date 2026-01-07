import sys
input = sys.stdin.readline

N = int(input())
status = 'CY'

while N > 0:
    if (N - 3 < 0):
        N -= 1
    else:
        N -= 3

    if status == 'SK':
        status = 'CY'
    else:
        status = 'SK'

print(status)