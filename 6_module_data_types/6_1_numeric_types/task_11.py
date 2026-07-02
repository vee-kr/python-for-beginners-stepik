num_1, num_2, num_3 = int(input()), int(input()), int(input())
mx, mn = max(num_1, num_2, num_3), min(num_1, num_2, num_3)
print(mx, (num_1 + num_2 + num_3 - mx - mn), mn, sep='\n')
