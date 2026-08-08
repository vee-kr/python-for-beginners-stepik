def print_fio(name, surname, patronymic):
    print(surname[0] + name[0] + patronymic[0])


name, surname, patronymic = input().upper(), input().upper(), input().upper()

print_fio(name, surname, patronymic)
