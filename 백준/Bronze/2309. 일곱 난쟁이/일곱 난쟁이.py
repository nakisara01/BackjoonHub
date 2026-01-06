arr = []
for _ in range(9):
    arr.append(int(input()))

total = sum(arr)

fake1 = fake2 = 0

for i in range(9):
    for j in range(i+1, 9):
        if total - (arr[i] + arr[j]) == 100:
            fake1 = arr[i]
            fake2 = arr[j]

arr.remove(fake1)
arr.remove(fake2)

arr.sort()

for x in arr:
    print(x)