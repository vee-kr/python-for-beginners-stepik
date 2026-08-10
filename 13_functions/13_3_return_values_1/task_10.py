def merge(list1, list2):
    list1.extend(list2)
    list1.sort()
    return list1


list_1, list_2 = [int(i) for i in input().split()], [int(k) for k in input().split()]
print(merge(list_1, list_2))
