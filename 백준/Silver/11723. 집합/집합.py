import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    order = list(input().split())

    if order[0] == "check":
        if order[1] in arr:
            print(1)
        else:
            print(0)
    
    elif order[0] == "all":
        arr = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]

    elif order[0] == "empty":
        arr = []

    elif order[0] == "add":
        if order[1] not in arr:
            arr.append(order[1])

    elif order[0] == "remove":
        if order[1] in arr:
            arr.remove(order[1])
    
    elif order[0] == "toggle":
        if order[1] in arr:
            arr.remove(order[1])
        else:
            arr.append(order[1])
    
    else:
        print("error")
    