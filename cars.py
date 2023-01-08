import panik_core as pk


class SportsCar:
    def __init__(self, window, model):
        self.model = model
        self.win = window

        self.load_car()

    def load_car(self):
        self.car_body = pk.Image(f"assets/cars/{self.model}/car1.png")
        self.car = pk.Element(self.car_body, 300, 300, 750)

    def rotate(self):
        mx, my = pk.Mouse.mouse_pos()
        self.car.point_towards(mx, my)

    def update(self, dt):
        # self.rotate()
        self.car.x += 100 * dt
        self.win.blit([self.car])
