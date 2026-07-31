num, total_num = int(input()), []
curr_num = int(input())
for _ in range(num - 1):
    next_num = int(input())
    total = curr_num + next_num
    total_num.append(total)
    curr_num = next_num

print(total_num)
