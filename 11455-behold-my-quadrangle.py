for _ in range(int(input())):
    nums = [int(x) for x in input().split()]
    nums.sort()

    if nums[0] == nums[3]:
        status =  "square"
    elif nums[0] == nums[1] and nums[2] == nums[3]:
        status =  "rectangle"
    elif sum(nums[:3]) >= nums[3]:
        status = "quadrangle"
    else:
        status =  "banana"

    print(status)
    
