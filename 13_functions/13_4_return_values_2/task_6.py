def is_prime(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return len(divisors) == 2 and num != 1


def get_next_prime(num):
    cur_num = num + 1
    while is_prime(cur_num) == False:
        cur_num += 1

    return cur_num


num = int(input())

print(get_next_prime(num))
