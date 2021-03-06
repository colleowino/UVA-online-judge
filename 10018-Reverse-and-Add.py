def revAdd(num, passes=1):
    a = int(num)
    b = int(num[::-1])
    total = a + b
    s_total = str(total)
    # print(a, b)
    if (s_total == s_total[::-1]):
        # print(True)
        return [passes, total]
    else:
        return revAdd(str(total), passes + 1)


for i in range(int(input())):
    num = input()
    res = revAdd(num)
    print(res[0], res[1])
