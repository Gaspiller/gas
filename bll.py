# 核心算法
import random

from Model import LocalModel


class GameCodeControler:
    def __init__(self):
        self.__list_merge = []
        self.__map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.__list_space = []

    @property
    def map(self):
        return self.__map

    # 矩阵转置
    def __rotate_list(self):
        for i in range(len(self.map) - 1):
            for j in range(i + 1, len(self.map)):
                self.map[j][i], self.map[i][j] = self.map[i][j], self.map[j][i]

    # 1.1将0往右移
    def __zero_to_right(self):
        for i in range(len(self.list_merge) - 1, -1, -1):
            if self.list_merge[i] == 0:
                del self.list_merge[i]
                self.list_merge.append(0)

    # 1.2将0往左移
    def __zero_to_left(self):
        for i in range(len(self.list_merge)):
            if self.list_merge[i] == 0:
                del self.list_merge[i]
                self.list_merge.insert(0, 0)

    # 2.1合并相同的元素
    def __mix_same_left(self):
        for i in range(len(self.list_merge) - 1):
            if self.list_merge[i] == self.list_merge[i + 1]:
                self.list_merge[i] += self.list_merge[i + 1]
                del self.list_merge[i + 1]
                self.list_merge.append(0)

    def __mix_same_right(self):
        for i in range(len(self.list_merge) - 1, -1, -1):
            if self.list_merge[i] == self.list_merge[i - 1]:
                self.list_merge[i] += self.list_merge[i - 1]
                del self.list_merge[i - 1]
                self.list_merge.insert(0, 0)

    # 3.1定义函数，将二位列表map中的0向左移
    def move_left(self):
        for line in self.map:
            self.list_merge = line
            self.__zero_to_left()
            self.__mix_same_right()

    # 3.2定义函数，将二位列表map中的0向右移动
    def move_right(self):
        for line in self.map:
            self.list_merge = line
            self.__zero_to_right()
            self.__mix_same_left()

    # 3.3定义函数，将二位列表map中的0向下移动
    def move_down(self):
        self.__rotate_list()
        self.move_right()
        self.__rotate_list()

    # 3.4定义函数，将二维列表map中的0向上移动
    def move_up(self):
        self.__rotate_list()
        self.move_left()
        self.__rotate_list()

    def new_number(self):
        self.__list_space = self.__new_local()
        loc = random.choice(self.__list_space)
        self.map[loc.x][loc.y] = 4 if random.randint(1, 10) == 1 else 2

    def __new_local(self):
        self.__list_space.clear()
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == 0:
                    self.__list_space.append(LocalModel(i, j))
        return self.__list_space

    def is_game_over(self):
        if len(self.__list_space) > 0:
            return False

        for i in range(len(self.map)):
            for j in range(len(self.map) - 1):
                if self.map[i][j] == self.map[i][j + 1] and self.map[j][i] == self.map[j + 1][i]:
                    return False
        return True
