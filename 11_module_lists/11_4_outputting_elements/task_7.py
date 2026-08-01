num, strings, searches = int(input()), [], []
for _ in range(num):
    strings.append(input())

k = int(input())
for _ in range(k):
    searches.append(input())

for string in strings:
    total = 0
    for search in searches:
        if search.lower() in string.lower():
            total += 1
    if total == k:
        print(string)
