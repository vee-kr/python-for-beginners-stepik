num, cube_numbers = int(input()), []
for _ in range(num):
    cube_number = int(input()) ** 3
    cube_numbers.append(cube_number)

print(cube_numbers)
