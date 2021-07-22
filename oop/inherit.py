# 继承
class vehicle():

    def __init__(self, brand):
        self.brand = brand

    def __repr__(self) -> str:
        return f'当前Car的品牌为：{self.brand}\n'


car1 = vehicle("奔驰")
print(car1)


class bicycle(vehicle):
    def type(self):
        print("单车...")


class train(vehicle):
    def type(self):
        print("火车...")


# 多态
bye = bicycle("小蓝车")
bye.type()
tn = train("高铁")
tn.type()
