text, last_cost, new_cost = input(), 0, 0
for char in text:
    last_cost += ord(char) * 3

last_letters = 'eyopaxcETOPAHXCBM'
new_letters = 'еуорахсЕТОРАНХСВМ'

for i in range(len(last_letters)):
    if last_letters[i] in text:
        text = text.replace(last_letters[i], new_letters[i])

for char in text:
    new_cost += ord(char) * 3

print(f"Старая стоимость: {last_cost}🐝")
print(f"Новая стоимость: {new_cost}🐝")
