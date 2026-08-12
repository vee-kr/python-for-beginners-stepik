def is_password_good(password):
    upper = [i for i in password if i.isupper()]
    lower = [i for i in password if i.lower()]
    digits = [i for i in password if i.isdigit()]

    if len(password) >= 8 and len(upper) >= 1 and len(lower) >= 1 and len(digits) >= 1:
        return True
    return False


text = input()

print(is_password_good(text))
