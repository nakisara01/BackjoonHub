X=int(input())
Y=int(input())


if X>0 and X<=1000:
    if Y>0 and Y<=1000:
        print("1")
    elif Y<0 and Y>=-1000:
        print("4")
elif X<0 and X>=-1000:
    if Y>0 and Y<=1000:
        print("2")
    elif Y<0 and Y>=-1000:
        print("3")