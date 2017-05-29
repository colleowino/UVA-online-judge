n = int(input())
totals = 0
for i in range(n):
    line = input().split()
    if len(line) > 1:
        totals += int(line[1])
    else:
        print(totals)
