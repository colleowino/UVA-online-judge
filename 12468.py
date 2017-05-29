# from math import fabs
while True:
    c_channel, n_channel = map(int, input().split())
    if c_channel == -1 and n_channel == -1:
        break
    diff = abs(n_channel - c_channel)

    if n_channel > c_channel:
        alt = c_channel+(99-n_channel)+1 #+1 coz of 0 channel num
    else:
        alt = n_channel+(99-c_channel)+1 #+1 coz of 0 channel num

    # print(alt,diff)
    print(min(alt,diff))

    # if diff > alt:
        # print(alt)
    # else:
        # print(diff)




