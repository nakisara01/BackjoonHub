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
result = []
    
A.sort()

find_ = [0 for i in find]

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for i in find:
    result.append(binary_search(A, i, 0, N-1))

print(*result)