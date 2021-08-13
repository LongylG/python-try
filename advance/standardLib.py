# 标准库

import itertools
from typing import DefaultDict, List
from collections import defaultdict
from collections import OrderedDict
from collections import Counter
from collections import deque
from collections import namedtuple
import base64
import hashlib
import heapq
import random


# base64
sEncode = base64.b64encode("hello world".encode())
print(sEncode)
sDecode = base64.b64decode(sEncode).decode()
print(sDecode)

# collections 容器数据类型模块

# deque：双端队列，是列表的替代实现。Python中的列表底层是基于数组来实现的，而deque底层是双向链表，因此当你需要在头尾添加和删除元素是，deque会表现出更好的性能，渐近时间复杂度为$O(1)$。
User = namedtuple('user', ['name', 'age', 'sex'])
user1 = User('david', 18, '男')
print(user1)

# namedtuple：命令元组，它是一个类工厂，接受类型的名称和属性列表来创建一个类。
dp1 = deque()
dp1.append(1)
dp1.append("2")
dp1.append(True)
print(dp1)
dp1.pop()
print(dp1)
dp1.popleft()
print(dp1)

# Counter：dict的子类，键是元素，值是元素的计数，它的most_common()方法可以帮助我们获取出现频率最高的元素。Counter和dict的继承关系我认为是值得商榷的，按照CARP原则，Counter跟dict的关系应该设计为关联关系更为合理。
c1 = Counter('12322123412')
print(c1.most_common(3))

# OrderedDict：dict的子类，它记录了键值对插入的顺序，看起来既有字典的行为，也有链表的行为。
od = OrderedDict()
od.setdefault(key='b', default=11)
od.setdefault(key='c', default=11)
od.update(a=1, b=2)
print(od)

# defaultdict：类似于字典类型，但是可以通过默认的工厂函数来获得键对应的默认值，相比字典中的setdefault()方法，这种做法更加高效。
dd = DefaultDict(c=11)
dd.update(a=1, b=2)
dd.setdefault('d', 22)
print(dd)

# hashlib 哈希函数模块提供了对哈希函数的封装，通过使用md5、sha1、sha256等类
# 字符串摘要
print(hashlib.md5('hello world'.encode()).hexdigest())
# 文件摘要
md5Hasher = hashlib.md5()
with open('1.txt', 'r') as file:
    data = file.read(512)
    while data:
        md5Hasher.update(data.encode())
        data = file.read(512)
print(md5Hasher.hexdigest())
# 修改文件做对比
md5Hasher2 = hashlib.md5()
with open('1.txt', 'a+') as file:
    file.write('1111')
    data = file.read(512)
    while data:
        md5Hasher2.update(data)
        data = file.read(512)
print(md5Hasher2.hexdigest())

# heapq模块实现了堆排序算法，如果希望使用堆排序，尤其是要解决TopK问题（从序列中找到K个最大或最小元素）
list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
print(heapq.nlargest(2, list1))
print(heapq.nsmallest(2, list1))
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
# 找出价格最高的三只股票
print(heapq.nlargest(3, list2, key=lambda x: x['price']))
# 找出持有数量最高的三只股票
print(heapq.nlargest(3, list2, key=lambda x: x['shares']))


# itertools - 迭代工具模块
# 产生ABCD的全排列
for value in itertools.permutations('ABCD'):
    print(value)

# 产生ABCDE的五选三组合
for value in itertools.combinations('ABCDE', 3):
    print(value)

# 产生ABCD和123的笛卡尔积
for value in itertools.product('ABCD', '123'):
    print(value)

# 产生ABC的无限循环序列
it = itertools.cycle(('A', 'B', 'C'))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# random - 随机数和随机抽样模块
# 这个模块我们之前已经用过很多次了，生成随机数、实现随机乱序和随机抽样，下面是常用函数的列表。
# getrandbits(k)：返回具有k个随机比特位的整数。
print(random.getrandbits(2))
# randrange(start, stop[, step])：从range(start, stop, step) 返回一个随机选择的元素，但实际上并没有构建一个range对象。
print(random.randrange(1, 10, 2))
# randint(a, b)：返回随机整数N满足a <= N <= b，相当于randrange(a, b+1)。
print(random.randint(1, 10))
# choice(seq)：从非空序列seq返回一个随机元素。 如果seq为空，则引发IndexError。
print(random.choice([1, 2, 3, 4, 5]))
# choices(population, weight=None, *, cum_weights=None, k=1)：从population中选择替换，返回大小为k的元素列表。 如果population为空，则引发IndexError。
print(random.choices([1, 2, 3, 4, 5], weights=[1, 2, 3, 4, 5], k=5))  # 概率
print(random.choices([1, 2, 3, 4, 5], cum_weights=[1, 2, 3, 6, 9], k=5))
# shuffle(x[, random])：将序列x随机打乱位置。
list2 = [1, 2, 3, 4, 5]
random.shuffle(list2)
print(list2)
# sample(population, k)：返回从总体序列或集合中选择k个不重复元素构造的列表，用于无重复的随机抽样。
print(random.sample([1, 2, 3, 4, 5], 2))
# random()：返回[0.0, 1.0)范围内的下一个随机浮点数。
# expovariate(lambd)：指数分布。
print('-----------------指数分布--------------------')
list3 = list()
for i in range(10):
    list3.append(int(random.expovariate(0.1)))
list3.sort()
print(list3)
# gammavariate(alpha, beta)：伽玛分布。
print('-----------------伽玛分布--------------------')
list4 = list()
for i in range(10):
    list4.append(int(random.gammavariate(2.00, 10.00)))
list4.sort()
print(list4)
# gauss(mu, sigma) / normalvariate(mu, sigma)：正态分布。
print('-----------------正态分布--------------------')
list5 = list()
for i in range(10):
    list5.append(int(random.gauss(2.00, 10.00) /
                     random.normalvariate(2.00, 10.00)))
list5.sort()
print(list5)
# paretovariate(alpha)：帕累托分布。
print('-----------------帕累托分布--------------------')
list6 = list()
for i in range(10):
    list6.append(int(random.paretovariate(0.1)))
list6.sort()
print(list6)
# weibullvariate(alpha, beta)：威布尔分布。
print('-----------------威布尔分布--------------------')
list7 = list()
for i in range(10):
    list7.append(int(random.weibullvariate(2.1, 1.9)))
list7.sort()
print(list7)
