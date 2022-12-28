import panik_core as pk


class Player(pk.Element):
    def __init__(self, win, map):
        self.win = win
        self.map = map
        self.load_anims()
        self.ww, self.wh = self.win.winsize
        super().__init__(self.still["3"], self.ww/2, self.wh/2, 750)
        self.add_colision("player", 0, 110, 130, 30)
        
        # player data
        self.direction = "3"
        self.movement = pk.Vec2()

    def load_anims(self):
        self.idle = {
            "1": pk.Animation("assets/player/idle/idle1"),
            "2": pk.Animation("assets/player/idle/idle2"),
            "3": pk.Animation("assets/player/idle/idle3"),
            "4": pk.Animation("assets/player/idle/idle4")
        }
        self.still = {
            "1": pk.Image("assets/player/still/still1.png"),
            "2": pk.Image("assets/player/still/still2.png"),
            "3": pk.Image("assets/player/still/still3.png"),
            "4": pk.Image("assets/player/still/still4.png")
        }
        self.walk = {
            "1": pk.Animation("assets/player/walk/walk1"),
            "2": pk.Animation("assets/player/walk/walk2"),
            "3": pk.Animation("assets/player/walk/walk3"),
            "4": pk.Animation("assets/player/walk/walk4")
        }
 
    def input(self, dt): 
        k = pk.Keys.get()

        if k[pk.kW]:
            self.movement.y = -1
            # self.y -= 300 * dt
        elif k[pk.kS]:
            self.movement.y = 1
            # self.y += 300 * dt
        else:
            self.movement.y=0
            
        if k[pk.kA]:
            self.movement.x = -1
            # self.x -= 300 * dt
        elif k[pk.kD]:
            self.movement.x = 1
            # self.x += 300 * dt
        else:
            self.movement.x=0
            
    
    def move(self, dt):
        if self.movement.magnitude() > 0:
            self.movement.normalize()
        self.try_move_x_tilemap(self.movement.x * 300 * dt, self.map.dev_tools_map)
        self.try_move_y_tilemap(self.movement.y * 300 * dt, self.map.dev_tools_map)
        self.win.camara.x += ((self.x-self.ww/2)-self.win.camara.x)/.3*dt
        self.win.camara.y += ((self.y-self.wh/2)-self.win.camara.y)/.3*dt

    def update(self, dt):
        self.input(dt)
        self.move(dt)
        self.win.blit([self])
