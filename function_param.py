def print_max(a, b):
    if a > b:
        print(a, "is maximum")
    elif a == b:
        print(a, "is equal to", b)
    else:
        print(b, "is maximum")

print_max(3, 5)

x, y = 3, 7
print_max(x, y)
