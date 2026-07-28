text = input()
if text.count('f') == 1:
    print(-1)
elif text.count('f') == 0:
    print(-2)
else:
    text = text.replace('f', '@', 1)
    index_f = text.find('f')
    print(index_f)
