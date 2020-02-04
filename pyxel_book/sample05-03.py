import pyxel
import random
from typing import List

WIDTH = 128
HEIGHT = 128
IMG_NO = 0
ENEMY_NO = 1


class Enemy:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)


class App:
    my_x = 0
    my_y = 0
    interval = 30
    cnt = 0
    enemyList: List[Enemy] = []

    def __init__(self):
        pyxel.init(WIDTH, HEIGHT)
        pyxel.load("mychara.pyxres")
        pyxel.run(self.update, self.draw)

    def makeEnemy(self):
        self.enemyList.append(Enemy())

    def checkTimer(self):
        bRet = False
        self.cnt = (self.cnt + 1) % self.interval
        if self.cnt == 0:
            bRet = True
        return bRet

    def isCollision(self, _i, _x, _y):
        bRet = False
        my_x = _x + 8
        my_y = _y + 8
        if (
            (self.enemyList[_i].x <= my_x)
            and (self.enemyList[_i].x + 16 >= my_x)
            and (self.enemyList[_i].y <= my_y)
            and (self.enemyList[_i].y + 16 >= my_y)
        ):
            bRet = True
        return bRet

    def update(self):
        self.my_x = pyxel.mouse_x
        self.my_y = pyxel.mouse_y
        if self.checkTimer():
            self.makeEnemy()
        for i in reversed(range(0, len(self.enemyList))):
            if self.isCollision(i, self.my_x, self.my_y) == True:
                del self.enemyList[i]

    def draw(self):
        pyxel.cls(7)
        for i in reversed(range(0, len(self.enemyList))):
            x = self.enemyList[i].x
            y = self.enemyList[i].y
            pyxel.blt(x, y, 1, 0, 0, 16, 16, 0)
        pyxel.blt(self.my_x, self.my_y, IMG_NO, 0, 0, 16, 16, 0)


App()
