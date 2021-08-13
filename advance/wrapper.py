from functools import wraps
import time
import random


def spend_time(func):
    # 定义一个带装饰功能（记录被装饰函数的执行时间）的函数
    # 因为不知道被装饰的函数有怎样的参数所以使用*args和**kwargs接收所有参数
    # 在Python中函数可以嵌套的定义（函数中可以再定义函数）
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}执行耗时{end-start:.3f}秒')
        return result
    return wrapper


# 可取消装饰器
def spend_time2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'装饰器参数：{self}')
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}执行耗时{end-start:.3f}秒')
        return result
    return wrapper


# 参数化
class SpendTime:

    def __init__(self, type) -> None:
        self.type = type

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f'类型{self.type}')
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f'{func.__name__}执行耗时{end-start:.3f}秒')
            return result
        return wrapper


@ spend_time
def eat(food):
    print(f'正在吃{food}')
    time.sleep(random.randint(1, 10))


@ spend_time2
def eat2(food):
    print(f'正在吃{food}')
    time.sleep(random.randint(1, 10))


@SpendTime("fruit")
def eat3(food):
    print(f'正在吃{food}')
    time.sleep(random.randint(1, 10))


def eat4(food):
    print(f'正在吃{food}')
    time.sleep(random.randint(1, 10))


eat("苹果")
# 取消装饰器
eat2 = eat2.__wrapped__
eat2("香蕉")
eat3("芒果")
eat4 = SpendTime("夏季水果")(eat4)
eat4("哈密瓜")
