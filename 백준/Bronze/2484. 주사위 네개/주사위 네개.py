import sys
input = sys.stdin.readline

def calc_prize(dice):
    freq = [0] * 7
    
    for x in dice:
        freq[x] += 1

    if 4 in freq:
        num = freq.index(4)
        return 50000 + num * 5000

    if 3 in freq:
        num = freq.index(3)
        return 10000 + num * 1000

    if freq.count(2) == 2:
        pair_nums = [i for i in range(1, 7) if freq[i] == 2]
        return 2000 + pair_nums[0] * 500 + pair_nums[1] * 500

    if 2 in freq:
        num = freq.index(2)
        return 1000 + num * 100
    
    return max(dice) * 100


N = int(input())
max_prize = 0

for _ in range(N):
    dice = list(map(int, input().split()))
    prize = calc_prize(dice)
    if prize > max_prize:
        max_prize = prize

print(max_prize)