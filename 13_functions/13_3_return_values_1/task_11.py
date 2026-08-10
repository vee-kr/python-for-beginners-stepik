def quick_merge(num):
    result = []
    for _ in range(num):
        result += [int(i) for i in input().split()]

    result.sort()
    return result


num = int(input())
print(*quick_merge(num))
