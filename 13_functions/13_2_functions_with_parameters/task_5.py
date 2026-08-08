def draw_triangle(fill, base):
    for i in range(1, base // 2 + 1):
        print(fill * i)
    for k in range(base // 2 + 1, 0, -1):
        print(fill * k)


fill, base = input(), int(input())
draw_triangle(fill, base)
