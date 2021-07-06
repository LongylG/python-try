# 字典：键值对，以{}或者dict函数或者生成式创建

user = {
    "jack": {"age": 18, "sex": "male"},
    "tom": {"age": 17, "sex": "female"}
}

print('user:'+str(user))
print(user.get("jack").get("age"))
user.pop("jack")
print(user)
k, v = user.popitem()
print(k, v)
user.setdefault("aaa", "aaa")
user.update(user)
print(user)


# dict函数
user2 = dict(name='mary', age=18, sex='female')
print('user2:'+str(user2))

# dict+zip
user3 = dict(zip("abcd", "1234"))
print('user3:'+str(user3))

# 生成式
