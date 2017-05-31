import re
while True:
    try:
        line = input()
        if len(line) > 1:
            changes = 0
            while bool(re.search('[ ]{2}',line)):
                changes += 1
                line = re.sub('[ ]{2}',' ',line)
            print(changes)

    except EOFError:
        break


