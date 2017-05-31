chants = {}
for _ in range(int(input())):
    title = input()
    chant = input()
    chants[title] = chant
for _ in range(int(input())):
    line = input()
    print(chants[line])


