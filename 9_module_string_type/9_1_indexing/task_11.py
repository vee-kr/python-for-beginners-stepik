text, count_vowels, count_consonants = input(), 0, 0
for char in text:
    if char in 'ауоыиэяюеАУОЫИЭЮЯЕ':
        count_vowels += 1
    elif char in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        count_consonants += 1

print('Количество гласных букв равно', count_vowels)
print('Количество согласных букв равно', count_consonants)
