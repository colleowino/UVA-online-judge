n = int(input())
two = "two"
for i in range(n):
    word = input()
    if len(word) > 3:
        print(3)
    else:
        score = 0
        for w in range(3):
            if two[w] == word[w]:
                score += 1
        if score > 1:
            print(2)
        else:
            print(1)

            

