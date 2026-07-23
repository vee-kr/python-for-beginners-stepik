text, total, largest = input(), 0, ''
for char in text:
    if text.count(char) >= total:
        total = text.count(char)
        largest = char

print(largest)
