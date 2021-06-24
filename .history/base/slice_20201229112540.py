strs = ["a", "b", "c", "d", "e"]

"""
支持正/负向索引，正向从0开始，负向从-1开始
slice[start,end,step]
切片时不包含end元素,step默认为1
"""
print(strs[::2])
print(strs[:2])
print(strs[2:])
print(strs[-2:])
print(strs[:-2])


# 矩阵转置
def transpose(arr):
    return [list(row) for row in zip(*arr)]


list1 = [[1, 4, 3], [1, 5, 7]]
print(transpose(list1))

# 矩阵逆转

list2 = [[1, 2, 4], [4, 2, 1]]


def invert(arr):
    return [row[::-1] for row in arr]


print(invert(list2))
