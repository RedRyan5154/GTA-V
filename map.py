import panik_core as pk


class Map:
    def __init__(self, win):
        self.win = win
        self.map_parent = pk.Parent(0, 0)

        road_tileset = pk.TileSet("assets/tilesets/road_tileset.png")
        asphalt_tileset = pk.TileSet("assets/tilesets/asphalt_tileset.png")
        outdoor_walls_tileset = pk.TileSet("assets/tilesets/outdoors_stuff_tileset.png")
        outdoor_walls_tileset.load()
        grass_sand_tileset = pk.TileSet("assets/tilesets/grass-sand_tileset.png")

        # dev stuff
        dev_tools_tileset = pk.TileSet("assets/tilesets/dev_stuff.png")
        self.dev_tools_map = pk.TileMap(
            "assets/map_colisions.csv",
            16,
            dev_tools_tileset.load(),
            750,
            0,
            0,
            self.map_parent,
        )
        self.dev_tools_map.id = "dev"
        self.map_roads = pk.TileMap(
            "assets/map_roads.csv",
            16,
            road_tileset.load(),
            750,
            0,
            0,
            self.map_parent,
        )
        self.map_asphalt = pk.TileMap(
            "assets/map_asphalt.csv",
            16,
            asphalt_tileset.load(),
            750,
            0,
            0,
            self.map_parent,
        )
        self.map_outdoor_walls = pk.TileMap(
            "assets/map_outdoor walls.csv",
            16,
            outdoor_walls_tileset.load(),
            750,
            0,
            0,
            self.map_parent,
        )
        self.map_grass_sand = pk.TileMap(
            "assets/map_grass-sand.csv",
            16,
            grass_sand_tileset.load(),
            750,
            0,
            0,
            self.map_parent,
        )

    def update(self, dt):
        self.dev_tools_map.hide = not self.win.devmode
        self.win.blit(
            [
                self.map_roads,
                self.map_asphalt,
                self.map_outdoor_walls,
                self.map_grass_sand,
                self.dev_tools_map,
            ]
        )
