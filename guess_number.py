#猜数字游戏
import random

#guess函数
def guess(num):
    count = 0
    while True:
        count += 1
        number = int(input('请输入你心中的数字：'))
        if num == number:
            print('恭喜你，你猜了{0}次终于猜对了数字{1}'.format(count,num))
            break
        elif number > num:
            print('你猜大了')
        elif number < num:
            print('你猜小了')

#生成一个1-100之间的随机数
num = random.randint(1,100)
guess(num)

'''
如果用户输入的数字超过了100，如果用户输入的不是数字，等等。记住，用户的输入都是不可靠的。
'''
