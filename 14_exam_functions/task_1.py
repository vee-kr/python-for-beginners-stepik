def draw_triangle():
    k = 1
    for _ in range(8):
        print(' ' * ((15 - k) // 2) + '*' * k)
        k += 2


draw_triangle()
