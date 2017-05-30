a, b = map(int,input().split())
menu = {}
for i in range(a):
    txt = input().split()
    menu[txt[0]] = txt[1]

for _ in range(b):
    food = input()
    # print("--",food)
    if food in menu:
        print(menu[food])
    else:
        end_l = food[-1]
        fend_l = food[-2]
        if end_l == "y" and fend_l not in "aeiou":
            print(food[:len(food)-1]+"ies")
        elif end_l in ["o","s","x"] or (fend_l+end_l) in ["ch","sh"]:
            print(food+"es")
        else:
            print(food+"s")


