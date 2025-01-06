frame = [[0] * 100 for _ in range(100)]

n = int(input())
axis = []
count = 0

for i in range(n):
    x, y = map(int, input().split())
    for j in range(10):
        for k in range(10):
            if frame[x+j][y+k] == 1:
                continue
            elif frame[x+j][y+k] == 0:
                frame[x+j][y+k] = 1
                count += 1
                
                
print(count)