def print_max(x,y):
    '''打印两个数的最大数
    这两个数必须是整数'''
    x = int(x)
    y = int(y)

    if x > y:
        print(x,'is maximum')
    else:
        print(y,'is maximum')

print_max(3,7)
print(print_max.__doc__)


