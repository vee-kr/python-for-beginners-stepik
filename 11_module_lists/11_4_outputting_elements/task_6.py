num, strings = int(input()), []
for _ in range(num):
    strings.append(input())

search = input().lower()
for string in strings:
    if search in string.lower():
        print(string)
