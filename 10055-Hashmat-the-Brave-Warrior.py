import sys
for i in sys.stdin:
    if len(i) > 1:
        a,b = map(int, i.split())
        print(abs(b-a))
