def lower_bound(arr, x):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] >= x:
            hi = mid
        else:
            lo = mid + 1
    return lo

def upper_bound(arr, y):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] > y:
            hi = mid
        else:
            lo = mid + 1
    return lo

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
node = list(map(int, input().split()))
node.sort()
res = []

for i in range(M):
    x, y = map(int, input().split())
    lo = lower_bound(node, x)
    hi = upper_bound(node, y)
    res.append(hi-lo)

print(*res, sep="\n")