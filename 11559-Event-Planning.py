while True:
    try:
        input_ = input()
        if input_ == '' or len(input_.split()) < 4:
            break

        n,b,h,w = map(int,input_.split())
        costs = []

        for _ in range(h):
            cost = int(input())*n
            days = [x for x in input().split() if int(x) >= n]
            if cost <= b and len(days) > 0:
                costs.append(cost)

        if len(costs) == 0:
            print("stay home")
        else:
            print(min(costs))
    except EOFError:
        exit()
