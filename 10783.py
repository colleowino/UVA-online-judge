n = int(input())
for i in range(n):
    a = int(input())
    b = int(input())

    total = 0
    for j in range(a,b+1):
        if j % 2 != 0:
            total += j

    print("Case",str(i+1)+":",total)
    
