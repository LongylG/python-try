# 列表[]-由相同数据类型组成的数据序列
# 元组()-由不同数据类型组成的数据序列，定义后类型和值均不可变
# 集合 无序性、互异性、确定性
arr = (0, True, 'hello world')
arr2 = (11, 22)
arr3 = arr + arr2
print(arr[0])
print(11 in arr)
print(11 in arr3)
print(arr[2])


# 修改元组会报错
try:
    arr[0] = 1
except TypeError:
    print("元组不可变")
arr = []

for i in range(10):
    arr.append(i)

# list函数创建数组
msg = list('hello world')
print(msg)
print(msg.index('o'))
print(msg.index('o', 4))


# 列表生成式
arr1 = [x for x in range(5)]
print(arr1)


arr2 = [x+y for x in 'xyz' for y in '123']
print(arr2)

nested_arr = [[0]*3] * 3
nested_arr[0][0] = 1
nested_arr[0][1] = 2
print(nested_arr)

# http://www.pythontutor.com/ 代码执行可视化
nested_arr2 = [[0]*3 for _ in range(3)]
nested_arr2[0][0] = 1
nested_arr2[0][1] = 2
print(nested_arr2)


set1 = {1, 1, 2, 3}
set2 = set([2, 2, 3])
set3 = set('hello world')
print(set1)
print(set2)
print(set3)
for i in set1:
    print(i)
