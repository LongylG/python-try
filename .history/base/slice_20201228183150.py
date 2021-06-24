strs = ["a","b","c","d","e"]

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