# 函数
def my_sum(n, m):
    return n + m


a = 1
b = 2
print(my_sum(a, b))

# 带默认参值


def power(n=1):
    return 2 << n


print(power())


# 可变参数，支持任意个参数

def my_sum(*arg):
    total = 0
    for i in arg:
        total += i
    return total


print(my_sum())

print(my_sum(1, 2, 3, 4))
