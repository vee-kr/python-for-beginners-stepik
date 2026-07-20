text = input()
for i in range(1, len(text) + 1):  # 1
    print(text[-i])

# -----------------------------------

for i in range(len(text) - 1, -1, -1):  # 2
    print(text[i])
