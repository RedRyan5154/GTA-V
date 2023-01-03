import panik_core as pk


class Player(pk.Element):
    def __init__(self, win, map):
        self.win = win
        self.map = map
        self.load_anims()
        self.ww, self.wh = self.win.winsize
        super().__init__(self.still["1"], self.ww / 2, self.wh / 2, 750)
        self.add_colision("player", 0, 110, 130, 30)

        # player data
        self.direction = "1"
        self.deg = 0

        pointer = pk.Image("assets/hud/pointer.png")
        self.pointer = pk.Element(pointer, 0, 0, 750)
        pk.Mouse.hide()

    def load_anims(self):
        self.idle = {
            "1": pk.Animation("assets/player/idle/idle1"),
            "2": pk.Animation("assets/player/idle/idle2"),
            "3": pk.Animation("assets/player/idle/idle3"),
            "4": pk.Animation("assets/player/idle/idle4"),
        }
        self.still = {
            "1": pk.Image("assets/player/still/still1.png"),
            "2": pk.Image("assets/player/still/still2.png"),
            "3": pk.Image("assets/player/still/still3.png"),
            "4": pk.Image("assets/player/still/still4.png"),
        }
        self.walk = {
            "1": pk.Animation("assets/player/walk/walk1"),
            "2": pk.Animation("assets/player/walk/walk2"),
            "3": pk.Animation("assets/player/walk/walk3"),
            "4": pk.Animation("assets/player/walk/walk4"),
        }

    def input(self, dt):
        if 1:
            self.deg = self.point_towards(self.pointer.x, self.pointer.y)
            if self.deg < 45 and self.deg > 0 or self.deg > -45 and self.deg < 0:
                self.direction = "1"
            elif (
                self.deg > 135 and self.deg < 180 or self.deg < -135 and self.deg > -180
            ):
                self.direction = "2"
            elif self.deg > 45 and self.deg < 135:
                self.direction = "4"
            elif self.deg < -45 and self.deg > -135:
                self.direction = "3"
            self.rotation = 0
            k = pk.Keys.get()

            if k[pk.kSHIFT]:
                sprint = 1
            else:
                sprint = 0

            if k[pk.kW]:
                res = self.try_move_towards_tilemap(
                    self.pointer.x,
                    self.pointer.y,
                    (200 + (150 if sprint else 0)) * dt,
                    self.map.dev_tools_map,
                )
                self.deg = res[4]
                self.animate(self.walk[self.direction], (0.075 if sprint else 0.125))
            elif k[pk.kS]:
                res = self.try_move_towards_tilemap(
                    self.pointer.x,
                    self.pointer.y,
                    (-150 + (-100 if sprint else 0)) * dt,
                    self.map.dev_tools_map,
                )
                self.deg = res[4]
                self.animate(self.walk[self.direction], (0.075 if sprint else 0.125))

            if k[pk.kA]:
                self.try_move_in_direction_tilemap(
                    self.deg + 90, 150 * dt, self.map.dev_tools_map
                )[4]
                if not any([k[pk.kW], k[pk.kS]]):
                    self.animate(self.walk[self.direction], 0.15)
            elif k[pk.kD]:
                self.try_move_in_direction_tilemap(
                    self.deg - 90, 150 * dt, self.map.dev_tools_map
                )[4]
                if not any([k[pk.kW], k[pk.kS]]):
                    self.animate(self.walk[self.direction], 0.15)

            if not any([k[pk.kW], k[pk.kS], k[pk.kA], k[pk.kD]]):
                self.animate(self.idle[self.direction], 0.35)

    def camera(self, dt):
        mx, my = pk.Mouse.mouse_pos()
        self.pointer.x, self.pointer.y = mx + self.win.camara.x, my + self.win.camara.y
        self.win.camara.x += ((self.x - self.ww / 2) - self.win.camara.x) / 0.3 * dt
        self.win.camara.y += ((self.y - self.wh / 2) - self.win.camara.y) / 0.3 * dt

    def update(self, dt):
        self.input(dt)
        self.camera(dt)
        self.win.blit([self, self.pointer])
