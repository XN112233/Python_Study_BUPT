import string
import random
import argparse

def evaluate_password(password,show_info=True):
    result = False
    password_state = 0b00000

    for char in password:
        if char in string.ascii_uppercase: #char.isupper()
            password_state |= 0b10000
        elif char in string.ascii_lowercase:
            password_state |= 0b01000
        elif char in string.digits:
            password_state |= 0b00100
        else:
            password_state |= 0b00010

    if len(password) >=8:
        password_state |= 0b00001

    if password_state == 0b11111:
        if show_info:
            print('密码符合要求！')
        result = True
    else:
        if show_info:
            prompt = '密码不符合要求，'
            if password_state & 0b00001 == 0:
                prompt += '长度不足8，'
            if password_state & 0b10000 == 0:
                prompt += '没有包含大写符号，'
            if password_state & 0b01000 == 0:
                prompt += '没有包含小写符号，'
            if password_state & 0b00100 == 0:
                prompt += '没有包含数字，'
            if password_state & 0b00010 == 0:
                prompt += '没有包含标点，'
            prompt = prompt[:-1]
            print(prompt)
    return result

def generate_password():
    all_char_set = string.printable[:-6]
    all_char_set *= 9   #可重复
    result = random.sample(all_char_set, k=9)
    return ''.join(result)

def create_password(pass_length, confuse=False):
    result = ''
    result += random.choice(string.ascii_uppercase)
    result += random.choice(string.ascii_lowercase)
    result += random.choice(string.digits)
    result += random.choice(string.punctuation)
    if confuse:
        result += 'Il'
        result += ''.join(random.sample(string.printable[:-6] * pass_length, pass_length - 6))
    else:
        result += ''.join(random.sample(string.printable[:-6] * pass_length, pass_length - 4))
    result = ''.join(random.sample(result, pass_length))
    return result

def main_userinput():
    while 1:
        password = input('请输入密码:')

        if evaluate_password(password):
            break

def main_genpassword():
    while 1:
        password = generate_password()
        if evaluate_password(password,show_info=False):
            print(f'新生成密码为：{password}')
            break

#命令行加参数执行
def main():
    parser = argparse.ArgumentParser(description='Generate new password.')
    parser.add_argument('-l', '--length', type=int, default=9, help='length of password (default: 9)')
    parser.add_argument('-c', '--confuse', action='store_true', help='use confuse characters (I & l)')
    args = parser.parse_args()

    for i in range(1):
        print(f'新生成的密码为：{create_password(args.length, args.confuse)}')

# main_userinput()
# main_genpassword()
main()

