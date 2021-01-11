#游戏界面逻辑模块
from bll import GameCodeControler


class GameView:
    def __init__(self):
        self.gcc = GameCodeControler()

    def start(self):
        self.gcc.new_number()
        self.gcc.new_number()
        self.__draw_map()

    def main(self):
        self.start()
        self.__update()

    def __update(self):
        while True:
            dir = input('请输入方向')
            if dir == 's':
                self.gcc.move_up()
            elif dir == 'w':
                self.gcc.move_down()
            elif dir == 'd':
                self.gcc.move_left()
            elif dir  == 'a':
                self.gcc.move_right()
            self.gcc.new_number()
            self.__draw_map()
            if self.gcc.is_game_over():
                print('游戏结束')



    def __draw_map(self):
        for i in self.gcc.map:
            for item in i:
                print(item,end='\t')
            print()


