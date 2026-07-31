alphabet = list()
for i in range(26):
    char = chr((ord('a') + i)) * (i + 1)
    alphabet.append(char)

print(alphabet)
