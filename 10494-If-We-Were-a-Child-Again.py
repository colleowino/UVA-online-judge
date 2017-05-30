while True:
    try:
        intro = input()
        if len(intro) > 1:
            a,b,c = intro.split()
            if b =="/":
                print(int(a)//int(c))
            else:
                print(int(a)%int(c))

    except EOFError:
        break

