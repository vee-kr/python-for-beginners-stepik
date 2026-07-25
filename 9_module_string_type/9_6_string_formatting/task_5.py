current_day, current_weight = int(input()), float(input())
target_weight_today = 100 - (12 / 60 * current_day)
if current_weight > target_weight_today:
    print('Что-то пошло не так')
else:
    print("Все идет по плану")
print(f"#{current_day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {current_weight} кг, ЦЕЛЬ по ВЕСУ = {target_weight_today} кг")
