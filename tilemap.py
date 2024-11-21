from os import listdir, path

import pygame, pytmx, pyscroll

from config import Config

class Tilemap:
    def __init__(self, screen, player):
        self.screen = screen
        self.player = player

        self.tmx_data = pytmx.load_pygame('assets/levels/level1.tmx')  # Change to your TMX file
        map_layer = pyscroll.BufferedRenderer(
            data=pyscroll.TiledMapData(self.tmx_data),
            size=self.screen.get_size(),
        )
        self.player_group = pyscroll.PyscrollGroup(map_layer=map_layer)
        self.player_group.add(self.player)

    def update(self):
        self.player_group.center(self.player.rect.center)
        self.player_group.draw(self.screen)

    def get_collidable_tiles(self):
        collidable_tiles = []
        collision_layer = self.tmx_data.get_layer_by_name("Collision")

        # Loop through each tile in the collision layer
        for x, y, gid in collision_layer:
            if gid:  # gid == 0 means there's no tile at this location
                # Create a pygame.Rect for each collidable tile
                rect = pygame.Rect(
                    x * self.tmx_data.tilewidth,
                    y * self.tmx_data.tileheight,
                    self.tmx_data.tilewidth,
                    self.tmx_data.tileheight
                )
                collidable_tiles.append(rect)
        return collidable_tiles