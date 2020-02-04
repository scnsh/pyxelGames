import pyxel
import pyxelChara as Chara
from typing import List

WIDTH = 128
HEIGHT = 128


class App:
    my_x = 0
    my_y = 0
    interval = 30
    cnt = 0
    enemyList: List[Chara.Enemy] = []

    def __init__(self):
        pyxel.init(WIDTH, HEIGHT)
        pyxel.load('mychara.pyxres')
        self.myChara = Chara.MyChara()
        pyxel.run(self.update, self.draw)

    def makeEnemy(self):
        self.enemyList.append(Chara.Enemy(WIDTH, HEIGHT))

    def checkTimer(self):
        bRet = False
        self.cnt = (self.cnt + 1) % self.interval
        if(self.cnt == 0):
            bRet = True
        return bRet

    def update(self):
        self.my_x = pyxel.mouse_x
        self.my_y = pyxel.mouse_y
        if self.checkTimer():
            self.makeEnemy()

        for i in reversed(range(0, len(self.enemyList))):
            if self.isCollision(i, self.my_x, self.my_y):
                self.myChara.startAnimation()
                self.enemyList[i].startAnimation()
            if self.enemyList[i].delete_flg:
                del self.enemyList[i]

    def isCollision(self, _i, _x, _y):
        bRet = False
        my_x = _x + 8
        my_y = _y + 8
        if not self.enemyList[_i].ani_flg and \
                not self.enemyList[_i].delete_flg:
            if (self.enemyList[_i].x <= my_x
                    and self.enemyList[_i].x + 16 >= my_x
                    and self.enemyList[_i].y <= my_y
                    and self.enemyList[_i].y + 16 >= my_y):
                bRet = True
        return bRet

    def drawMap(self):
        tm = 0
        w = int(WIDTH / 8)
        h = int(HEIGHT / 8)
        pyxel.bltm(0, 0, tm, 0, 0, w, h)

    def draw(self):
        pyxel.cls(7)
        self.drawMap()
        for i in reversed(range(0, len(self.enemyList))):
            x = self.enemyList[i].x
            y = self.enemyList[i].y
            if not self.enemyList[i].delete_flg:
                self.enemyList[i].drawImage(x, y)

        self.myChara.drawImage(self.my_x, self.my_y)


App()
