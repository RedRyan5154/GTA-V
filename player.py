import panik_core as pk


class Player:
    def __init__(self, win):
        self.win = win

    def input(self, dt, map):
        k = pk.Keys.get()

        if k[pk.kW]:
            # map.map_parent.y += 300 * dt
            self.win.camara.y -= 300 * dt
        elif k[pk.kS]:
            # map.map_parent.y -= 300 * dt
            self.win.camara.y += 300 * dt
        if k[pk.kA]:
            # map.map_parent.x += 300 * dt
            self.win.camara.x -= 300 * dt
        elif k[pk.kD]:
            # map.map_parent.x -= 300 * dt
            self.win.camara.x += 300 * dt

    def update(self, dt, map):
        self.input(dt, map)
