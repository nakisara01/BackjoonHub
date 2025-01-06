x, y, w, h = map(int, input().split())

min_distance = min(x, w - x, y, h - y)

print(min_distance)
