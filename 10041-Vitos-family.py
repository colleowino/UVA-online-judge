for _ in range(int(input())):
    nums = [int(x) for x in input().split(' ')]
    n = nums[0]
    streets = nums[1:]
    streets.sort()
    diff = streets[n//2]
    total = 0
    for s in streets:
        total += abs(diff - s)
    print(total)
