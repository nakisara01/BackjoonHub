n = int(input())

group = 0
apart = []
house_counts = []

for _ in range(n):
    row = list(map(int, input()))
    apart.append(row)
    if len(row) != n:
        print("apart group size error")
        exit()

def DFS(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return 0
    if apart[x][y] == 1:
        apart[x][y] = 0
        count = 1
        count += DFS(x, y - 1)
        count += DFS(x - 1, y)
        count += DFS(x + 1, y)
        count += DFS(x, y + 1)
        return count
    return 0

for i in range(n):
    for j in range(n):
        count = DFS(i, j)
        if count > 0:
            house_counts.append(count)
            group += 1

print(group)
for count in sorted(house_counts):
    print(count)
