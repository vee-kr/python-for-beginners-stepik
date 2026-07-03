string_1, string_2, string_3 = input(), input(), input()
len_1, len_2, len_3 = len(string_1), len(string_2), len(string_3)
max_len, min_len = max(len_1, len_2, len_3), min(len_1, len_2, len_3)
middle_len = (len_1 + len_2 + len_3) - max_len - min_len
if max_len - middle_len == middle_len - min_len:
    print('YES')
else:
    print('NO')
