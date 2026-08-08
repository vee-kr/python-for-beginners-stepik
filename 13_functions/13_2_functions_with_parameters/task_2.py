def print_case_counts(s):
    lowers, uppers = 0, 0
    for char in s:
        if char.islower():
            lowers += 1
        elif char.isupper():
            uppers += 1

    print(f"Букв в верхнем регистре: {uppers}")
    print(f"Букв в нижнем регистре: {lowers}")


s = input()
print_case_counts(s)
