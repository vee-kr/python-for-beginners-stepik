text, count = input(), 0
for i in range(10):
    cur_digit = text.count(str(i))
    count += cur_digit

print(count)
