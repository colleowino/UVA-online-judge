while True:
    try:
        intro = input()
        if len(intro) > 1:
            a,b = map(int,intro.split())
            smoked = a

            while a >= b:
                discount =  a%b
                divi = a //b

                a = divi+discount
                smoked += divi

            print(smoked)

    except EOFError:
        break

