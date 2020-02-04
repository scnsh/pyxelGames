import pyxel

WIDTH = 256
HEIGHT = 256
IMG_NO = 0
pyxel.init(WIDTH, HEIGHT)
pyxel.load("mychara.pyxres")
pyxel.cls(1)
pyxel.blt(WIDTH / 2, HEIGHT / 2, IMG_NO, 0, 0, 16, 16, 0)
pyxel.show()
