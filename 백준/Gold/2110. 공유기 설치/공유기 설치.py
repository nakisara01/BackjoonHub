import sys
input = sys.stdin.readline

N, C = map(int, input().split())
address = []

for _ in range(N):
    tmp = int(input())
    address.append(tmp)

address.sort()

start = 0
end = address[N-1]

def can_place(distance):
    cnt = 1
    last = address[0]

    for house in address[1:]:
        if house - last >= distance:
            cnt += 1
            last = house
                
        if cnt == C:
            return True

    return False

left = 1
right = address[-1] - address[0]
ans = 0

while left <= right:
    mid = (left + right) // 2
    
    if can_place(mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)