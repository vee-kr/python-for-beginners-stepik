text = input()
longest = text
shortest = longest

while text != 'КОНЕЦ':
    shortest = min(shortest, text)
    longest = max(longest, text)
    text = input()

print(f"Минимальная строка ⬇️: {shortest}")
print(f"Максимальная строка ⬆️: {longest}")
