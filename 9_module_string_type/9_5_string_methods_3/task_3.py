car_licence_plate, flag = input(), True
alph = car_licence_plate[0] + car_licence_plate[4:6]
for char in alph:  # 1
    if char not in 'АВЕКМНОРСТУХ':
        flag = False
if flag == True and car_licence_plate[1:4].isdigit() and car_licence_plate[6] == '_' and car_licence_plate[
    7:].isdigit() and 9 <= len(car_licence_plate) <= 10:
    print('YES')
else:
    print('NO')

# -----------------------------------------
if (car_licence_plate[0] in 'АВЕКМНОРСТУХ'  # 2
        and car_licence_plate[1:4].isdigit()
        and car_licence_plate[4] in 'АВЕКМНОРСТУХ'
        and car_licence_plate[5] in 'АВЕКМНОРСТУХ'
        and car_licence_plate[6] == '_'
        and car_licence_plate[7:].isdigit()
        and 9 <= len(car_licence_plate) <= 10):
    print('YES')
else:
    print('NO')
