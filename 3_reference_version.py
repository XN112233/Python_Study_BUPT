# 整个读取->在适当位置插入数据->整个写回文件
#初始化 rank.txt 文件
rank_info_list = ['Tom 15', 'Alice 16', 'Bob 20']
with open('rank.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(rank_info_list))

#插入新用户信息
new_name = 'Mike'
new_score = 15

#整个读取
with open('rank.txt', 'r', encoding='utf-8') as f:
    rank_info_list = f.read().split('\n')

#适当位置插入
index = 0
while index < len(rank_info_list):
    if new_score < int(rank_info_list[index].split()[1]):
        break
    index += 1

rank_info_list.insert(index, new_name + ' ' + str(new_score))

#整个写回文件
with open('rank.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(rank_info_list))