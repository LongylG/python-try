class cat:
    # 指定对象允许的属性，禁用动态属性
    __slots__ = ('__name', 'color')

    # 只能有一个init构造方法
    def __init__(self, color):
        self.__name = "12"
        self.color = color

    @staticmethod
    def eat():
        print("猫猫爱吃鱼")

    @property
    def name1(self):
        return self.__name

    @name1.setter
    def name1(self, name):
        self.__name = name

    def __repr__(self):
        """
        修改print方法打印内容
        """
        return f'cat颜色:{self.color}'


cat1 = cat("黑白")
cat.eat
# 属性装饰器调用
cat1.name1 = '121'
print(cat1.name1)
# 动态设置属性
try:
    cat1.age = 12
    print(cat1.age)
except AttributeError:
    print("已禁用动态属性")

# print(cat1.__name)
# _类名__属性名可以访问到私有属性
print(cat1._cat__name)
