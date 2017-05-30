k = 1
n = int(input())
for i in range(n):
    total_walls = int(input())
    walls = [int(x) for x in input().split()]

    high_jump = 0
    low_jump = 0

    for i in range(total_walls-1):
        if walls[i] > walls[i+1]:
            high_jump += 1
        elif walls[i+1] > walls[i]:
            low_jump +=1

    print("Case",str(k)+":",low_jump,high_jump)
    k+=1

