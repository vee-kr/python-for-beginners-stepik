def is_palindrome(text):
    string = ''  # 1
    for char in text:
        if char.isalpha():
            string += char.lower()
    return string == string[::-1]

    symbols = [' ', '.', ',', '!', '-', '?']  # 2
    for symbol in symbols:
        text = text.replace(symbol, '')
    return text.lower() == text.lower()[::-1]


text = input()
print(is_palindrome(text))
