# 位置参数、命名关键字参数
import random


def sum(x, y, z):
    return x+y+z


print(sum(1, 2, 3))
print(sum(x=1, y=2, z=3))

# 可变参数


def sum2(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(sum2(1, 2, 3))

# 可变参数+位置参数


def sum3(*args, **kwargs):
    sum = 0
    for i in args:
        sum += i
    for k in kwargs.keys():
        print(k)
    for v in kwargs.values():
        sum += v
    return sum


def calc(*args, func, **kwargs):
    return func(*args, **kwargs)


print(sum3(1, a=2, c=3))
# 调用函数需要跟上括号，函数作为参数不需要括号
print(calc(1, func=sum3, a=2, c=3))
print(calc(1, 2, 3, func=sum2))


# lambda
def lmd(x, y): return x+y % 2


xArrs = [1, 2, 3, 4, 5, 6]
filterArrs = filter(lambda x: x % 3 == 0, xArrs)
print(lmd(1, 5))
print('---------------------')
for i in filterArrs:
    print(i)
