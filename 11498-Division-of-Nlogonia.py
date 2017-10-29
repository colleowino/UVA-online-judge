while True:
    n = int(input())
    if n == 0:
        break
    Ox,Oy = [int(x) for x in input().split()]
    for _ in range(n):
        x,y = [int(x) for x in input().split()]
        # origins divisa
        if x == Ox or y == Oy:
            print("divisa")
        # East
        elif x > Ox:
            if y > Oy:
                print("NE")
            else:
                print("SE")
        # West
        else:
            if y > Oy:
                print("NO")
            else:
                print("SO")
