money, counter = int(input()), 0

while money >= 25:
    counter += 1
    money -= 25
while money >= 10:
    counter += 1
    money -= 10
while money >= 5:
    counter += 1
    money -= 5
while money >= 1:
    counter += 1
    money -= 1

print(counter)
