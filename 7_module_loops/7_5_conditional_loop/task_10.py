hour_1, min_1, hour_2, min_2 = int(input()), int(input()), int(input()), int(input())
start, end = hour_1 * 60 + min_1, hour_2 * 60 + min_2
while start <= end:
    hour, minutes = start // 60, start % 60
    if hour < 10 <= minutes:
        print('0', hour, ':', minutes, sep='')
    elif minutes < 10 <= hour:
        print(hour, ':', '0', minutes, sep='')
    elif minutes < 10 and hour < 10:
        print('0', hour, ':', '0', minutes, sep='')
    else:
        print(hour, ':', minutes, sep='')

    start += 1
