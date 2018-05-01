import sys

c = 1
for line in sys.stdin:
    line = line.rstrip()
    output = ""
    for a in line:
        if a == '"':
            if c % 2 != 0:
                output += '``'
            else:
                output += "''"
            c += 1
        else:
            output += a

    print(output)
