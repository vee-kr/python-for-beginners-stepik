num = int(input())
last, mid, first = num % 10, num % 100 // 10, num // 100
mx, mn, total = max(last, mid, first), min(last, mid, first), last + mid + first
if mx - mn == (total - mx - mn):
    print("The number's interesting")
else:
    print("The number isn't interesting")
