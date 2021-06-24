a = 1
b = 4


'''
太久没用容易混淆，mark一下
运算规则
按位或
1|1=1; 1|0=1; 0|1=1; 0|0=0

按位异或
0^0=0; 0^1=1; 1^0=1; 1^1=0;

取反
~1=0; ~0=1;

按位与
0&0=0; 0&1=0; 1&0=0; 1&1=1;
'''

#算数运算符
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)  # 整除

#逻辑运算符
print(~-1)  # 按位取反   ~x=-（x+1）
print(a ^ b)  # 按位异或
print(a | b)  # 按位或
print(a & b)
print(a and b)
print(not b)
print(b or a)
print(a in [2,3])

##位移运算符
print(a >> 2)
print(a << 2)


#比较运算符
print(a > b)
print(a == b)

# 成员运算符
print(a and b)

