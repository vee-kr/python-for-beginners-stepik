text = input()
new_text = ''
for i in range(len(text)):
    if i % 3 == 0:
        continue
    new_text += text[i]

print(new_text)
