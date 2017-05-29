n = int(input())
for i in range(n):
    nums = [int(x) for x in input().split()]
    result = True

    if nums[0] > 20:
        result = False
    
    if nums[1] > 20:
        result = False

    if nums[2] > 20:
        result = False

    print("Case",str(i+1)+":","good" if result else "bad")

