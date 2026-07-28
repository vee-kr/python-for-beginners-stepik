text = input()
index_h, r_index_h = text.find('h'), text.rfind('h')

between_h = text[index_h + 1: r_index_h]
between_h = between_h[::-1]

print(text[:index_h + 1] + between_h + text[r_index_h:])
