n = 0
ref = {"HELLO":"ENGLISH",
       "HOLA":"SPANISH",
       "HALLO":"GERMAN",
       "BONJOUR":"FRENCH",
       "ZDRAVSTVUJTE":"RUSSIAN",
       "CIAO":"ITALIAN"}

while True:
    word = input()
    if word == "#":
        break

    if word in ref:
        print("Case",str(n+1)+":",ref[word])
    else:
        print("Case",str(n+1)+": UNKNOWN")
    n+= 1
    
