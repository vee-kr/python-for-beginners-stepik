def is_correct_bracket(text):
    while '()' in text:
        text = text.replace('()', '')
    if text.count('(') != text.count(')') or len(text) > 0:
        return False
    return True


brackets = input()

print(is_correct_bracket(brackets))
