num, cipher = int(input()), input()
for char in cipher:

    cur_code = ord(char)  # 1
    new_code = cur_code - num

    if (new_code >= ord('a')) and (new_code <= ord('z')):
        new_letter = chr(new_code)
        print(new_letter, end='')
    else:
        new_letter = chr((ord('z') - (num - (cur_code - ord('a')))) + 1)
        print(new_letter, end='')

    # ---------------------------------------------

    if new_code < ord('a'):  # 2
        new_letter = new_code + 26
        print(chr(new_letter), end='')
    else:
        print(chr(new_code), end='')
