mount1 = 100  # 整数
mount2 = 100.0  # 浮点数
arr = [1, 2, 3]  # 数组
arr2 = [[1, 2], [2, 3]]  # 二维数组
map = {"a": "1", "b": 1, "c": "123"}  # map
str1 = "hello word"
flag = True  # 0-False 1-Ture,可与数字相加
print(mount1)
print(mount2)
print(arr[0])
print(arr2[0][0])
print(map["a"])
print(str1)
print(flag)
print(flag + 1)

# 输出类型
print(type(mount1))
print(type(mount2))
print(type(arr))
print(type(arr2))
print(type(str1))
print(type(map))
print(type(flag))
# 判断变量是否属于该类型
print(isinstance(flag,str))

    
# 变量类型转换
print(int(mount2))
print(str(mount2))
print(int(flag))
print(str(flag))
print(chr(flag))
print(chr(65))


