def print_sorted_hyphen(s):
    words = s.split('-')
    words.sort()
    print(*words, sep='-')


text = input()
print_sorted_hyphen(text)
