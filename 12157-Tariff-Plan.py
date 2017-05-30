from math import ceil

case = 1
n = int(input())
for i in range(n):
    total_calls = input()

    calls = [int(x) for x in input().split()]
    mile = 0
    juice = 0

    for q in calls:
        if q % 30 == 0:
            mile += ((q//30)+1)*10
        else:
            mile += ceil(q/30)*10

        if q % 60 == 0:
            juice += ((q//60)+1)*15
        else:
            juice += ceil(q/60)*15

    best = 0
    # print("compare:",mile,juice)
    
    if mile < juice:
        best = mile
        chose = "Mile"
    elif juice < mile:
        best = juice
        chose = "Juice"
    else:
        best = juice
        chose = "Mile Juice"
    
    print("Case",str(case)+":", chose,best)
    case +=1

