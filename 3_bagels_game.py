from ast import arg
import random
import string
import os
import time
import argparse

def main():
    #定义常量
    all_digits = string.digits
    max_try = 6
    num_digits = 3

    #设置命令行参数
    # parser = argparse.ArgumentParser(description='Playing Bagels Game.')
    # parser.add_argument('-t', '--maxtry', type=int, default=6, help='max_try of bagel game (default: 6)')
    # parser.add_argument('-n', '--num', type=int, default=3, help='the number of digit (default: 3)')
    # args = parser.parse_args()

    #清屏并显示
    os.system('cls')
    name = input('请输入姓名：')
    print(f'我想好了一个{num_digits}位不重复的数字，你来猜猜看？')
    # print(f'我想好了一个{args.num}位不重复的数字，你来猜猜看？')

    target = ''.join(random.sample(all_digits,k=num_digits))
    # target = ''.join(random.sample(all_digits,k=args.num))

    #开始猜数
    round = 1
    start_time =  int(time.time())
    while True:
        while True:
            guess = input('> ')
            if len(guess) == num_digits and len(guess) == len(set(guess)) and guess.isdigit():
            # if len(guess) == args.num and len(guess) == len(set(guess)) and guess.isdigit():
                break
            else:
                print(f'请输入{num_digits}位不重复的数字！')
                # print(f'请输入{args.num}位不重复的数字！')

        if guess == target:
            end_time = int(time.time())
            
            #自己想的，老师给的参考版本另附
            #追加进入文本
            with open('E:/bagels/rank.txt','a',encoding='utf-8') as f:
                f.write(f'{name}\t{end_time-start_time}\n')
            #读取文本，生成排名
            with open('E:/bagels/rank.txt','r',encoding='utf-8') as f:
                content = f.read()
                content = content.split('\n')[:-1]
            ulist = []
            for con in content:
                uname , utime = con.split('\t')
                ulist.append((uname,utime))
            ulist.sort(key= lambda x:int(x[1]))
            urank = ulist.index((name,str(end_time-start_time)))+1
            #显示用户名，排名
            print(f'恭喜{name}猜对了！你真棒^_^ 总共猜了{round}次，用时{end_time-start_time}秒,排名{urank}名。')

            break
        else:
            print(get_clue(target, guess))

        if round == max_try:
        # if round == args.maxtry:
            print(f'您已经猜了{round}次，挑战失败！')
            break
        round += 1

def get_clue(target, guess):
    clue = ''

    for index in range(len(target)):
        if guess[index] == target[index]:
            clue += '√'
        elif guess[index] in target:
            clue += '?'
        else:
            clue += 'x'
    #clue顺序改造
    # clue =  ''.join(sorted(list(clue)))
    return clue


main()

# 待改进：
# 1.max_try num_digits 命令行输入参数(已完成)
# 2.固定max_try num_digits，用户输入姓名 ，根据成功后返回的秒数生成排名，告知排第几(已完成)


# a = random.sample(['red', 'red', 'red', 'red', 'blue', 'blue'], k=5)
# b = random.sample(['red', 'blue'], counts=[4,2], k=5)
# print(a,b)