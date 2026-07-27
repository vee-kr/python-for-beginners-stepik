text_1, text_2, text_3 = input(), input(), input()
largest = max(text_1, text_2, text_3)
smallest = min(text_1, text_2, text_3)

if smallest < text_2 < largest:
    middle = text_2
elif smallest < text_1 < largest:
    middle = text_1
else:
    middle = text_3

print(smallest, middle, largest)
