import pyxel

WIDTH = 128
HEIGHT = 128
IMG_NO = 0


class App:
    my_x = 0
    my_y = 0

    def __init__(self):
        pyxel.init(WIDTH, HEIGHT)
        pyxel.load("mychara.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        self.my_x = pyxel.mouse_x
        self.my_y = pyxel.mouse_y

    def draw(self):
        pyxel.cls(7)
        pyxel.blt(self.my_x, self.my_y, IMG_NO, 0, 0, 16, 16, 0)


App()
