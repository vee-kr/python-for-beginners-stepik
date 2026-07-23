text = input()
if text.find('f') == text.rfind('f') and text.find('f') != -1:  # 1
    print(text.find('f'))
elif text.find('f') == -1:
    print('NO')
else:
    print(text.find('f'), text.rfind('f'))

# ------------------------------------------
if text.count('f') == 0:  # 2
    print('NO')
elif text.count('f') == 1:
    print(text.find('f'))
else:
    print(text.find('f'), text.rfind('f'))
