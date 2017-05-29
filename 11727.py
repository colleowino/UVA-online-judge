n = int(input())
for i in range(n):
    nums = [int(x) for x in input().split()]
    nums.sort()
    print("Case",str(i+1)+":",nums[1])
