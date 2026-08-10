import math


def math_round_to_int(num):
    first_after_dot = str(num)[str(num).find('.') + 1]  # 1
    if int(first_after_dot) >= 5:
        return math.ceil(num)
    else:
        return math.floor(num)

    if num - int(num) >= 0.5:  # 2
        return math.ceil(num)
    else:
        return math.floor(num)


num = float(input())
print(math_round_to_int(num))
