def number_of_factors(num):
    total_factors = [i for i in range(1, num + 1) if num % i == 0]
    return len(total_factors)


num = int(input())
print(number_of_factors(num))
