import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Flappy Bird")

        pyxel.load("assets/flappybird.pyxres")

        self.score = 0
        self.player_x = 72
        self.player_y = -16
        self.player_vy = 0
        self.player_is_alive = True

        # pyxel.playm(0, loop=True) # play music

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_0):
            pyxel.quit()

        self.update_player()

    def update_player(self):

        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.player_vy = - 6

        self.player_y += self.player_vy
        self.player_vy = min(self.player_vy + 1, 8)

        if self.player_y > pyxel.height:
            if self.player_is_alive:
                self.player_is_alive = False
                # pyxel.play(3, 5) # play sound
            if self.player_y > 600:
                self.score = 0
                self.player_x = 72
                self.player_y = -16
                self.player_vy = 0
                self.player_is_alive = True

    def draw(self):
        pyxel.cls(12)

        # draw forest
        offset = pyxel.frame_count % 160
        for i in range(2):
            pyxel.blt(i * 160 - offset, 72, 0, 0, 16, 160, 48, 12)

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
        s = "SCORE {:>4}".format(self.score)
        pyxel.text(5, 4, s, 1)
        pyxel.text(4, 4, s, 7)


App()
