n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    lower = (a-b)//2
    higher = lower+b
    if lower+higher != a or lower < 0:
        print("impossible")
    else:
        print(higher,lower)
