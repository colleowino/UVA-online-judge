print("Lumberjacks:")
for i in range(int(input())):
    nums =[int(x) for x in input().split()]

    last_result =  1 if nums[1] > nums[0] else 0 #trend
    ordered = True
    # print("matched",last_result)
    
    for i in range(1,len(nums)-1):
        match =  1 if nums[i+1] > nums[i] else 0 #trend
        # print("matched",match)
        if match != last_result:
            ordered = False
            break

    if ordered:
        print("Ordered")
    else:
        print("Unordered")
