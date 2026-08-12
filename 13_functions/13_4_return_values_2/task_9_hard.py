def is_prime(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return len(divisors) == 2


def is_valid_password(password):
    digits_password = password.split(':')
    first, second, third = digits_password[0], int(digits_password[1]), int(digits_password[2])

    return len(digits_password) == 3 and first == first[::-1] and is_prime(second) and third % 2 == 0


password = input()
print(is_valid_password(password))
