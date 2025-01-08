x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

x_coords = [x1, x2, x3]
y_coords = [y1, y2, y3]

x4 = x1 if x_coords.count(x1) == 1 else (x2 if x_coords.count(x2) == 1 else x3)
y4 = y1 if y_coords.count(y1) == 1 else (y2 if y_coords.count(y2) == 1 else y3)

print(x4, y4)