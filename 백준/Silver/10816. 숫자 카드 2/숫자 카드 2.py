import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
if len(A) != N:
    print("List size error")
    exit()
M = int(input())
find = list(map(int, input().split()))
if len(find) != M:
    print("List size error")
    exit()

A.sort()

def binary_search(array, target, start, end, find_lower):
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            result = mid
            if find_lower:
                end = mid - 1
            else:
                start = mid + 1
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return result

def count_occurrences(array, target, n):
    lower = binary_search(array, target, 0, n - 1, find_lower=True)
    if lower == -1:
        return 0
    upper = binary_search(array, target, 0, n - 1, find_lower=False)
    return upper - lower + 1

for num in find:
    print(count_occurrences(A, num, N), end=' ')