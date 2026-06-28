color_1, color_2 = input(), input()
if color_1 == 'red' == color_2:
    print(color_1)
elif color_1 == 'yellow' == color_2:
    print(color_1)
elif color_1 == 'blue' == color_2:
    print(color_1)
elif (color_1 == 'red' and color_2 == 'blue') or (color_1 == 'blue' and color_2 == 'red'):
    print('purple')
elif (color_1 == 'red' and color_2 == 'yellow') or (color_1 == 'yellow' and color_2 == 'red'):
    print('orange')
elif (color_1 == 'blue' and color_2 == 'yellow') or (color_1 == 'yellow' and color_2 == 'blue'):
    print('green')
else:
    print('the mistake of color')
