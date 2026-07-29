num = int(input())
text = ''

alphabet = 'abcdefghijklmnopqrstuvwxyz'  # 1
chars = list(alphabet[:num])
print(chars)

for char in range(num):  # 2
    text += chr(ord('a') + char)
print(list(text))
