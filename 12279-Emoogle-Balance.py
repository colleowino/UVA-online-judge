q = 1
while True:
    n = int(input())
    if n == 0:
        break
    nums = [int(x) for x in input().split()]

    gave = 0
    didnot = 0

    for i in nums:
        if i == 0:
            gave += 1
        else:
            didnot += 1

    print("Case",str(q)+":",didnot-gave)
    q+=1
