while True:
    try:
        intro = input()
        if len(intro) > 1:
            a,b = map(int,intro.split())
            result = 0

            for i in range(1,a+1):
                result += i*(b**i)

            print(result)

    except EOFError:
        break

