num = int(input())
for hour in range(24):
    for minute in range(60):
        if hour ** num == minute:
            h, m = hour, minute
            if h < 10:
                h = '0' + str(h)
            else:
                h = str(h)
            if m < 10:
                m = '0' + str(m)
            else:
                m = str(m)
            print(h, m, sep=':')
