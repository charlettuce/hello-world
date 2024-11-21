import pygame
from numpy import array
from config import Config
import pytmx


def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))

class Player(pygame.sprite.Sprite):
    def __init__(self, window, character, code_runner):
        super().__init__()
        self.image = pygame.image.load("assets/player/player_" + str(character+1) + ".png") 
        self.window = window

        self.position = self.get_initial_position()
        self.rect = self.image.get_rect()
        self.rect.center = self.get_initial_position()
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self)

        self.code_runner = code_runner

    def get_initial_position(self):
        return array([self.window.get_size()[0]/2 - self.image.get_size()[0]/2, self.window.get_size()[1]/2 - self.image.get_size()[1]/2])

    def move(self, movement_vector):
        # block movement if player typing
        if self.code_runner.typing:
            return
        
        # move player
        self.rect.x += int(movement_vector[0])
        self.rect.y += int(movement_vector[1])

        # check collision
        if self.check_collision(self.rect):
            self.rect.x -= int(movement_vector[0])
            self.rect.y -= int(movement_vector[1])

    def check_collision(self, player_rect):
        map_width_in_pixels = self.tilemap.tmx_data.width * self.tilemap.tmx_data.tilewidth  - self.rect.width
        map_height_in_pixels = self.tilemap.tmx_data.height * self.tilemap.tmx_data.tileheight - self.rect.height

        if self.rect.x <= 0 or self.rect.x >= map_width_in_pixels:
                return True
        if self.rect.y <= 0 or self.rect.y >= map_height_in_pixels:
            return True

        for tile in self.tilemap.get_collidable_tiles():
            
            if player_rect.colliderect(tile):
                return True
            
        return False
    
    def parse_tilemap(self, tilemap):
        self.tilemap = tilemap