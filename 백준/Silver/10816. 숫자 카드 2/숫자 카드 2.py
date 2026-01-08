import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))

M = int(input())
count = list(map(int, input().split()))

cnt = {}

for card in cards:
    cnt[card] = cnt.get(card, 0) + 1
    
for x in count:
    print(cnt.get(x, 0), end=' ')