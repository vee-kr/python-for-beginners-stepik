text = input()
part_1 = text[:text.find('h')]
part_2 = text[text.rfind('h') + 1:]
print(part_1 + part_2)
