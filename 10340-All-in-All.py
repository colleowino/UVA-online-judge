while True:
    try:
        line = input().split(' ')
        matched = 0
        longer = line[1]
        for x in line[0]:
            if x in longer:
                matched += 1
                pos = longer.index(x)
                longer = longer[pos + 1:]
            else:
                break

        if (len(line[0]) == matched):
            print('Yes')
        else:
            print('No')

    except EOFError:
        break
