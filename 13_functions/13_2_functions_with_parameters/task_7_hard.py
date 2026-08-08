def print_symbol_counts(s):
    chars = []

    for char in s.lower():
        if char not in chars:
            chars.append(char)

    chars.sort()

    for char in chars:
        print(f"{char}: {s.lower().count(char)}")


text = input()
print_symbol_counts(text)
