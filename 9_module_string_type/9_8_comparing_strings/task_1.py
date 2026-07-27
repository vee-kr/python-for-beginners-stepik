shortest = input()
longest = shortest
for i in range(3):
    text = input()
    longest = max(longest, text)
    shortest = min(shortest, text)

result = ord(shortest[-1]) * ord(longest[-1])
print(result ** 2)
