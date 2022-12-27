import panik_core as pk
from map import Map
from player import Player


class Game:
    def __init__(self):
        self.win = pk.Window("My Window", 1920, 1080)
        self.win.showfps = True
        # self.win.setFullscreen()

        self.map = Map(self.win)
        self.player = Player(self.win)

    def run(self):
        run = 1

        while run:
            dt = self.win.tick(0)

            for event in pk.Events.get():
                if (
                    event.type == pk.QUIT
                    or event.type == pk.KEY_PRESSED
                    and event.key == pk.kQ
                ):
                    run = 0
                if event.type == pk.KEY_PRESSED:
                    if event.key == pk.kK:
                        self.win.devmode = not self.win.devmode

            self.player.update(dt, self.map)
            self.map.update(dt)
            self.win.render()


if __name__ == "__main__":
    game = Game()
    game.run()
