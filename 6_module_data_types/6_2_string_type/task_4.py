city_1, city_2, city_3 = input(), input(), input()
mx_len, mn_len = max(len(city_1), len(city_2), len(city_3)), min(len(city_1), len(city_2), len(city_3))
if mn_len == len(city_1):
    print(city_1)
elif mn_len == len(city_2):
    print(city_2)
else:
    print(city_3)
if mx_len == len(city_1):
    print(city_1)
elif mx_len == len(city_2):
    print(city_2)
else:
    print(city_3)
