text = input().split()
counter = 0
for i in range(len(text)):
    for k in range(i + 1, len(text)):
        if text[i] == text[k]:
            counter += 1
print(counter)
