for i in range(int(input())):
    line = input()
    total = 0
    counter = 0
    for c in line:
        if c == "O":
            counter +=1
            total += counter
        else:
            counter = 0
    print(total)
