
arr = (0, True, 'hello world')

print(arr[0])
print(arr[1])
print(arr[2])

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
