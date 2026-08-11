def convert_to_python_case(text):
    python_case = []  # 1
    last_up = 0
    for i in range(1, len(text)):
        if text[i].isupper():
            word = text[last_up:i].lower()
            last_up = i
            python_case.append(word)
        elif i == len(text) - 1:
            word = text[last_up:].lower()
            python_case.append(word)
    return python_case

    # --------------------------------

    new_text = ''  # 2
    for char in text:
        if char.isupper():
            new_text += '_' + char.lower()
        else:
            new_text += char
    return new_text[1:]


text = input()
answer = convert_to_python_case(text)

print(*answer, sep='_')
