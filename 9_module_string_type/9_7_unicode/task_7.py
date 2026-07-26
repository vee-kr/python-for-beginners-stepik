text = input()
for i in range(64):
    letter = chr(ord('А') + i)
    code_letter = ord('А') + i
    pattern = f"[u-{code_letter}]"
    if pattern in text:
        text = text.replace(pattern, letter)
        
print(text)
