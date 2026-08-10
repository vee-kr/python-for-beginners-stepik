def get_unique(numbers):
    unique_numbers = []
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)
    return unique_numbers


numbers = eval(input())
print(get_unique(numbers))
