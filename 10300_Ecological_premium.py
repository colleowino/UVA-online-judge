n = int(input())
for i in range(n):
    total_famers = int(input())
    total_cost = 0
    for j in range(total_famers):
        a,b,c = map(int, input().split())
        farmer_cost = ((a/b)*c)*b
        total_cost += farmer_cost
    print(int(total_cost))


