# list01 = [2, 0, 0, 2]
# # 定义函数，方阵转置
# def change_list(list):
#     for i in range(len(list) - 1):
#         for j in range(i + 1, len(list)):
#             list[j][i], list[i][j] = list[i][j], list[j][i]
#
# list_map = [
#     [2, 4, 0, 2],
#     [0, 2, 2, 0],
#     [0, 0, 0, 2],
#     [4, 0, 0, 4]
# ]
#
# # 1.1将0往右移
# def zero_to_right(list):
#     for i in range(len(list) - 1, -1, -1):
#         if list[i] == 0:
#             del list[i]
#             list.append(0)
#
#
# # 1.2将0往左移
# def zero_to_left(list):
#     for i in range(len(list) - 1):
#         if list[i] == 0:
#             del list[i]
#             list.insert(0, 0)
#
#
# # 2.1合并相同的元素
# def mix_same(list):
#     for i in range(len(list) - 1):
#         if list[i] == list[i + 1]:
#             list[i] += list[i + 1]
#             del list[i + 1]
#             list.append(0)
#
#
# # 3.1定义函数，将二位列表map中的0向左移
# def move_left(list):
#     global list01
#     for line in list:
#         list01 = line
#         zero_to_left(list01)
#
#
# # 3.2定义函数，将二位列表map中的0向右移动
# def move_right(list):
#     global list01
#     for line in list:
#         list01 = line
#         zero_to_right(list01)
#
#
# # 3.3定义函数，将二位列表map中的0向下移动
# def move_down(list):
#     change_list(list)
#     move_right(list)
#     change_list(list)
#
#
# # 3.4定义函数，将二维列表map中的0向上移动
# def move_up(list):
#     change_list(list)
#     move_left(list)
#     change_list(list)


list_map = [
    [2, 4, 0, 2],
    [0, 2, 2, 0],
    [0, 0, 0, 2],
    [4, 0, 0, 4]
]
import random
# 随机位置产生随机数字，计算出所有空位，随机选一个

print(list_space)




# 2 90%  4 10%
list_number = [2,2,2,2,2,2,2,2,2,4]
a = random.choice(list_number)
print(a)

list_map[p[0]][p[1]] = a