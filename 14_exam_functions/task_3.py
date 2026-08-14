from math import factorial


def compute_binom(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


n, k = int(input()), int(input())
print(compute_binom(n, k))
