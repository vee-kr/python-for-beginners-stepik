def get_month(language, number):
    en = ['', 'january', 'february', 'march', 'april', 'may', 'june',
          'july', 'august', 'september', 'october', 'november', 'december']
    ru = ['', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
          'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    if language == 'en':
        return en[number]
    else:
        return ru[number]


lang, num = input(), int(input())
print(get_month(lang, num))
