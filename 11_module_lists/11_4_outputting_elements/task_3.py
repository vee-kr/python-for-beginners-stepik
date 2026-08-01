num = int(input())
strings = list()
for _ in range(num):
    text = input()
    if text in strings:
        continue
    else:
        strings.append(text)

print(*strings, sep='\n')
