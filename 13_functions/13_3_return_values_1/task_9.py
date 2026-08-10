def find_all(target, symbol):
    result = []
    for i in range(len(target)):
        if target[i] == symbol:
            result.append(i)

    return result


target, symbol = input(), input()
print(find_all(target, symbol))
