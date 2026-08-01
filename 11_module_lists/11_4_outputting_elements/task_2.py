num = int(input())
negatives, zeros, positives = [], [], []
for _ in range(num):
    cur_num = int(input())
    if cur_num < 0:
        negatives.append(cur_num)
    elif cur_num == 0:
        zeros.append(cur_num)
    else:
        positives.append(cur_num)

print(*(negatives + zeros + positives), sep='\n')
