k = 1
n = int(input())
for i in range(n):
    nums = [int(x) for x in input().split()]
    print("Case",str(k)+":",max(nums[1:]))
    k+=1
    
