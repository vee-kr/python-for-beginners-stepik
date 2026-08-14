def is_pangram(text):
    alphabet = 'abcdefghijklmnopqrstu'
    for c in alphabet:
        if c not in text:
            return False
    return True


text = input().lower()
print(is_pangram(text))
