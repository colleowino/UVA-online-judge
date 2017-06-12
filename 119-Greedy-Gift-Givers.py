cases = 0
while True:
    try:
        nums = int(input())
        ordered = input().split()
        gifted = {}

        for name in ordered:
            gifted[name] = 0

        for _ in range(nums):
            line = input().split()
            name = line[0]
            total_given = int(line[1])
            total_receivers = int(line[2])

            if total_receivers > 0 and total_given > 0:
                gift_ratio = total_given//total_receivers 
                gifted[name] -= (gift_ratio*total_receivers) # keeps left overs

                for person in line[3:]:
                    gifted[person] += gift_ratio
            # else:
                # gifted[name] += int(total_given)

        if cases > 0:
            print("")

        for person in ordered:
            print(person,gifted[person])

        cases += 1
    
    except EOFError:
        exit()
