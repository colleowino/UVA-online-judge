for i in range(int(input())):
    line = list(map(int, input().split()))
    total = sum(line[1:])
    avg = total/line[0]
    above_avg = [x for x in line[1:] if x > avg]
    print("%.3f" % ((len(above_avg)/line[0])*100)+"%")
