import random

total = 0
# 求和1-100，步长为2
for i in range(1, 100, 2):
    total += i
print(total)

# 输出1-100区间整数
for x in range(101):
    print(f'生产随机数字:{x}')

the_number = random.randint(1, 100)
max = 100
min = 1
guess_total = 0
while True:
    guess_total += 1
    guess_number = int(input('请输入'+str(min)+'-'+str(max)+'内的一个整数：'))
    if(guess_number > the_number):
        if(guess_number < max):
            max = guess_number
    elif(guess_number < the_number):
        if(guess_number > min):
            min = guess_number
    else:
        print("congratulation,you are winner!")
        print(f"总共猜测次数：{guess_total}")
        break

