def is_prime(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return len(divisors) == 2 and num != 1


num = int(input())

print(is_prime(num))
