from datetime import datetime
import numpy as np

def count_dec_places(num):
    num_as_str = str(num)
    try:
        dec_index = num_as_str.index(".")
        dec = num_as_str[dec_index + 1:]
        return len(dec)
    except:
        return 0

def round_to(num, nrst, limit):
    """
    Rounds a number to the nearest tenth, quarter..., and makes sure to not exceed a given limit.
    """
    round_to_x_dec = count_dec_places(num)

    dec = num - int(num)
    dec_remainder = round(dec % nrst, round_to_x_dec)

    if dec_remainder == 0:
        return num
    if dec_remainder >= round(nrst / 2, round_to_x_dec):
        rounded_up = int(num) + (dec - dec_remainder) + nrst
        if rounded_up <= limit:
            return round(rounded_up, round_to_x_dec)
    rounded_down = int(num) + (dec - dec_remainder)
    return round(rounded_down if rounded_down <= limit else limit, round_to_x_dec)

def another_round_to(num, nrst):
    nrst = 1 / nrst
    return (int(nrst*num-0.5)+1) / nrst

for num in np.arange(0, 1, .01):
    first = another_round_to(num, .1)
    second = round_to(num, .1, 100)
    if first != second:
        print(num)
        print(first, " != ", second, sep="")




