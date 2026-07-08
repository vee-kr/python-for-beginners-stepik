num_1, num_2, counter = int(input()), int(input()), 0
for i in range(num_1, num_2 + 1):
    if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
        counter += 1
print(counter)
