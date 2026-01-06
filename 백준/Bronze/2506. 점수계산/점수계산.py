N = int(input())
test = list(map(int, input().split()))

score = 0
combo = 0

for x in test:
    if x == 1:
        combo += 1
        score += combo
    else:
        combo = 0

print(score)