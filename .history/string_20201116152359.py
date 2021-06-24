import os
s = '''hello
world
!'''
s2 = "1f431"
print(s, end='')  # 以‘’结尾,不换行
print(s, s2)

# 获取字符的ascii或者unicode
print(ord('中'))
print(ord('A'))

print("\141\142\143\x61\x62\x63", "\u4e2d\u56fd")


def get_suffix(file_path):
    index = file_path.rfind(".")
    return file_path[index + 1:] if index > 0 else ''


def get_suffix_fast(file_path):
    return os.path.splitext(file_path)
    # return file_path.split(".")


if __name__ == "__main__":
    print(get_suffix("test.png"))
    print(get_suffix_fast("/test/test.png.bak")[-1])
