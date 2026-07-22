text, count = input(), 0
for char in text:
    if char in 'qwertyuiopasdfghjklzxcvbnm':
        count += 1

print(count)
