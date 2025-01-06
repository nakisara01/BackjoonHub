n, m = map(int, input().split())

Frame = []
for _ in range(n):
    Row = list(map(int, input().split()))
    Frame.append(Row)

def DFS_iterative(x, y):
    stack = [(x, y)]
    size = 0
    while stack:
        cx, cy = stack.pop()
        if cx < 0 or cy < 0 or cx >= n or cy >= m:
            continue
        if Frame[cx][cy] == 1:
            Frame[cx][cy] = 0
            size += 1
            stack.append((cx - 1, cy))  # 상
            stack.append((cx + 1, cy))  # 하
            stack.append((cx, cy - 1))  # 좌
            stack.append((cx, cy + 1))  # 우
    return size

num_pictures = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if Frame[i][j] == 1:
            area = DFS_iterative(i, j)
            num_pictures += 1
            max_area = max(max_area, area)

print(num_pictures)
print(max_area)
