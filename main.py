import panik_core as pk
from map import Map
from player import Player



class Game:
    def __init__(self):
        self.win = pk.Window("My Window", 1080, 720)
        self.win.showfps = True
        self.win.setFullscreen()

        self.map = Map(self.win)
        self.player = Player(self.win, self.map)        
        

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
                    pk.quit()
                if event.type == pk.KEY_PRESSED:
                    if event.key == pk.kK:
                        self.win.devmode = not self.win.devmode

            self.map.update(dt)
            
            self.player.update(dt)
            # self.pointer.point_towards(self.win.wwidth/2, self.win.wheight/2)
            
            self.win.render()


if __name__ == "__main__":
    game = Game()
    game.run()
