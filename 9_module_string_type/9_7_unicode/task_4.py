weighest_word, largest = '', 0
for _ in range(4):
    text = input()
    total_cur = 0
    for char in text:
        total_cur += ord(char)
    if total_cur > largest:
        largest = total_cur
        weighest_word = text

print(weighest_word)
