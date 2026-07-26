text, total_cost = input(), 0
for char in text:
    total_cost += ord(char) * 3

print(f"Текст сообщения: '{text}'")
print(f"Стоимость сообщения: {total_cost}🐝")
