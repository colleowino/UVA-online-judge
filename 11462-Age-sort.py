import sys
input = sys.stdin.readline
while True:
    num = input().strip()
    if num == '0':
        break
    else:
        nums = [int(x) for x in input().strip().split(' ')]
        nums.sort()
        nums = [str(x) for x in nums]
        print(' '.join(nums))
