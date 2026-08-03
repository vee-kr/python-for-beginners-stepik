numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

smallest, largest = min(numbers), max(numbers)
index_smallest, index_largest = numbers.index(smallest), numbers.index(largest)

numbers.insert(index_smallest, largest)  # 1
del numbers[index_smallest + 1]
numbers.insert(index_largest, smallest)
del numbers[index_largest + 1]
print(*numbers)

# ------------

numbers[index_smallest], numbers[index_largest] = numbers[index_largest], numbers[index_smallest]  # 2
print(*numbers)
