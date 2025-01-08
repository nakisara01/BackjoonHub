n = int(input())

min_x = float('inf')
max_x = float('-inf')
min_y = float('inf')
max_y = float('-inf')

for _ in range(n):
    x, y = map(int, input().split())
    if x < min_x:
        min_x = x
    if x > max_x:
        max_x = x
    if y < min_y:
        min_y = y
    if y > max_y:
        max_y = y

if n == 1:
    area = 0
else:
    area = (max_x - min_x) * (max_y - min_y)

print(area)