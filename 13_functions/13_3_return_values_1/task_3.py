def get_days(month):
    if month in [2]:
        return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31


month = int(input())
print(get_days(month))
