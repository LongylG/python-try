import sys

"""
'r'	读取 （默认）
'w'	写入（会先截断之前的内容）
'x'	写入，如果文件已经存在会产生异常
'a'	追加，将内容写入到已有文件的末尾
'b'	二进制模式
't'	文本模式（默认）
'+'	更新（既可以读又可以写）
"""


def readtext(path):
    """
    简单读取纯文本
    """
    f = open(path, "r", encoding="utf-8")
    print(f.read())
    f.close


def appendText(path, content):
    """
    追加文本
    """
    with open(path, "a+") as f2:
        f2.write(content)
        # f2.close


def readTextByLine(path):
    f = open(path, "r")
    for line in f.readlines():
        print(line, end='')
    print("---------------------")
    f2 = open(path, "r")
    for line in f2:
        print(line, end='')


def copyFile(src_path, tagert_path):
    with open(src_path, "rb") as f1:
        data = f1.read()
    with open(tagert_path, "wb") as f2:
        f2.write(data)


# readTextByLine(".gitignore")
# appendText("1.txt", "\n2021-06-29")
copyFile("1.txt","2.txt")
