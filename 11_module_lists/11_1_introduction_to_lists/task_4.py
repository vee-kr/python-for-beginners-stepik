text = input()

chars_1 = ''  # 1
for i in range(0, len(text), 2):
    chars_1 += text[i]
print(list(chars_1))

chars_2 = list(text[::2])  # 2                            
print(chars_2)
