string_1 = input().split()
string_2 = input().split()

total = []
for i in range(len(string_1)):  # 1
    total.append(int(string_1[i]) + int(string_2[i]))

print(*total)

total = [int(string_1[i]) + int(string_2[i]) for i in range(len(string_1))]  # 2
print(*total)
