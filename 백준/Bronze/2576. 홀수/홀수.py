ans = 0
smaller = 100
for i in range(7):
    tmp = int(input())
    if tmp % 2 == 1:
        ans += tmp
        if tmp < smaller:
            smaller = tmp

if ans == 0:
    print(-1)
else:
    print(ans)
    print(smaller)