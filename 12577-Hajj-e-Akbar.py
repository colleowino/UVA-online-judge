ref = { "Hajj": "Akbar", "Umrah":"Asghar"}
n = 1
while True:
    line = input()
    if line == "*":
        break
    print("Case "+str(n)+":","Hajj-e-"+ref[line])
    n += 1
