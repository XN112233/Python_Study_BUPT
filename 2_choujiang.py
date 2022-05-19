import random
import time

#随机数
def chou_1(u_list):
    selected_user_info =  random.choice(u_list).split()
    print(f'恭喜中奖用户：{selected_user_info[0]} {selected_user_info[1]}')
    return selected_user_info[0]

#时间戳确定
def chou_2(u_list):
    while 1:
        try:
            idx = int(time.time() * 1000) % len(u_list) #毫秒对len取余 0-(len-1)
            print(f'\r{u_list[idx]}', end='') #\r覆盖从头输出
            time.sleep(0.001)
        except KeyboardInterrupt:
            break
    selected_user_info =  u_list[idx].split()
    #\r覆盖从头输出，这里输出内容无法覆盖原先内容，所以用空格占位
    print(f'\r恭喜中奖用户：{selected_user_info[0]} {selected_user_info[1]}         ')
    return selected_user_info[0]

#距离确定
def chou_3(u_list):
    while 1:
        rand_x = random.randint(0,10000) /10
        rand_y = random.randint(0,10000) /10 #增加一位精度 
        try:
            print(f'\r{rand_x},{rand_y}', end='') 
            time.sleep(0.1)
        except KeyboardInterrupt:
            break

    user_distance_list = []
    for user_info in u_list:
        uid, uname, ux, uy = user_info.split('\t') #多项赋值
        distance = int((int(ux) - rand_x) ** 2 + (int(uy) - rand_y) ** 2)
        user_distance_list.append((uid, uname, distance))

    user_distance_list.sort(key=lambda x:x[2])   #按照distance排序
    print(f'\r恭喜中奖用户：{user_distance_list[0][0]} {user_distance_list[0][1]}') 

def main():
    with open('2_users.txt', encoding='utf-8') as f:
        content =  f.read()

    user_list = content.split('\n') 
    chou_1(user_list)
    chou_2(user_list)
    chou_3(user_list)

main()
