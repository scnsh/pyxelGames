from random import randrange
from enum import Enum

import pyxel


class App:
    class State(Enum):
        TITLE = 0
        INGAME = 1
        RESULT = 2

    def __init__(self):
        pyxel.init(160, 120, caption="Flappy Bird")

        pyxel.load("assets/flappybird.pyxres")

        self.state = App.State.TITLE
        self.guide = "Click to start game!!"
        self.reset()

        pyxel.run(self.update, self.draw)

    def reset(self):
        self.score = 0
        self.player_x = 72
        self.player_y = 32
        self.player_vy = 0
        self.player_is_alive = True
        self.pipe = [((i+2) * 80, randrange(16, 88, 8), True) for i in range(4)]
        self.last_offset = 0

    def update(self):

        if pyxel.btnp(pyxel.KEY_0):
            pyxel.quit()

        if self.state in (App.State.TITLE, App.State.RESULT):
            if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                self.state = App.State.INGAME
                self.reset()
        else:
            if self.player_is_alive:
                self.update_player()

                for i, v in enumerate(self.pipe):
                    self.pipe[i] = self.update_pipe(*v)

            self.update_gravity()
            if self.player_y >= 96:
                if self.player_is_alive:
                    self.player_is_alive = False
                    self.player_y = 96
                self.state = App.State.RESULT

    def update_gravity(self):
        self.player_y = min(self.player_y + self.player_vy, 96)
        self.player_vy = min(self.player_vy + 1, 4)

    def update_player(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and self.player_is_alive:
            self.player_vy = -4

    def update_pipe(self, x, y, is_active):
        if is_active:
            if x + 8 >= self.player_x >= x - 8:
                if y + 16 >= self.player_y >= y - 16:
                    pyxel.play(3, 0)
                else:
                    self.player_is_alive = False
            elif self.player_x > x - 8:
                is_active = False
                self.score += 1

        x -= 2

        if x < -40:
            x += 320
            y = randrange(16, 88, 8)
            is_active = True

        return x, y, is_active

    def draw(self):
        pyxel.cls(12)

        # draw forest
        offset = pyxel.frame_count % 160 if self.player_is_alive else self.last_offset
        for i in range(2):
            pyxel.blt(i * 160 - offset, 72, 0, 0, 16, 160, 48, 12)
        self.last_offset = offset

        # draw pipe
        for x, y, is_active in self.pipe:
            for y_offset in range(0, 104, 8):
                if y_offset == y-16:
                    pyxel.blt(x, y_offset, 0, 32, 8, 16, 8, 12)
                elif y_offset == y+16:
                    pyxel.blt(x, y_offset, 0, 32, 0, 16, 8, 12)
                elif y_offset > y+16 or y_offset < y-16:
                    pyxel.blt(x, y_offset, 0, 48, 0, 16, 8, 12)

        # draw player
        pyxel.blt(
            self.player_x,
            self.player_y,
            0,
            16 if self.player_vy > 0 else 0,
            0,
            16,
            16,
            12,
        )

        # draw score
        if self.state is App.State.TITLE:
            pyxel.text(32, 16, self.guide, 1)
            pyxel.text(33, 16, self.guide, 7)
        elif self.state is App.State.INGAME:
            s = "SCORE {:>4}".format(self.score)
            pyxel.text(5, 4, s, 1)
            pyxel.text(4, 4, s, 7)
        elif self.state is App.State.RESULT:
            s = "RESULT {:>4}".format(self.score)
            pyxel.text(56, 48, s, 1)
            pyxel.text(57, 48, s, 7)
            pyxel.text(40, 64, self.guide, 1)
            pyxel.text(41, 64, self.guide, 7)


App()
