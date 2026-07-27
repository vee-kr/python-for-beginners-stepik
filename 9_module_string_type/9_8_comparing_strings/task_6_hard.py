num, book_last, flag = int(input()), input(), 'YES'

for _ in range(num - 1):
    book_next = input()
    surname_last = book_last[: book_last.find(' ')]
    surname_next = book_next[: book_next.find(' ')]

    title_book_last = book_last[book_last.find('«') + 1: book_last.find('»')]
    title_book_next = book_next[book_next.find('«') + 1: book_next.find('»')]

    if surname_next < surname_last or (surname_next == surname_last and title_book_next < title_book_last):
        flag = 'NO'
        break

    book_last = book_next
    title_book_last = title_book_next

print(flag)
