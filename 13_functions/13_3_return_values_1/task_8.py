def get_last_index(data, value):
    if value in data:
        for i in range(len(data) - 1, -1, -1):
            if data[i] == value:
                return i
    else:
        return 'ERROR!'


data, value = eval(input()), eval(input())

print(get_last_index(data, value))
