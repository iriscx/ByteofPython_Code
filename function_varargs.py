def total(a=5, *numbers, **phonebook):
    print('a',a)

    for item in numbers:
        print('item', item)
    for first, second in phonebook.items():
        print(first, second)

print(total(10,1,2,3,jack=1123,John=2231))

