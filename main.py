from numpy import array, dtype
import pygame
from sys import exit

from config import Config
from controls import Controls

from player import Player
from tilemap import Tilemap
from start import StartMenu
from code_runner import CodeRunner

from gui.text_button import TextButton

class Game:
    def __init__(self):       
        pygame.init()
        icon = pygame.image.load('icon.png')  # Make sure 'icon.png' exists in your working directory

        # Set the window icon
        pygame.display.set_icon(icon)

        self.screen = pygame.display.set_mode((Config.DEFAULT_WIN_WIDTH, Config.DEFAULT_WIN_HEIGHT)) # config.py
        self.clock = pygame.time.Clock()

        self.movement_vector = []
        self.menu_button = None

        self.setup_start() # show start menu first

        self.gameloop()

    def setup_start(self):
        self.state = "START"
        self.start = StartMenu(self.screen)

    def reset_game(self):
        pygame.display.set_caption(Config.GAME_PLAYING_CAPTION) 

        self.code_runner = CodeRunner(self.screen)
      
        self.player = Player(self.screen, self.start.selected_character, self.code_runner)
        self.tilemap = Tilemap(self.screen, self.player)

        self.player.parse_tilemap(self.tilemap)

        self.state = "GAME"
        self.code_runner.run_user_code("print(\"morning \") \ntime.sleep(1) \nprint(\"goodnight \")")
        #self.code_runner.run_user_code("print(\"morning goblin\") \nprint(\"goodnight goblin\")")
        #self.code_runner.run_user_code("input(\"brrr\")")
        
    def gameloop(self):
        while True:
            self.events()
            self.draw()

            pygame.display.update()
        

    def events(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.menu_button.collidepoint(event.pos):
                    print("clic")
                    self.start_state = "START"
                    self.state = "START"
                    self.setup_start()
                    
        
        keys = pygame.key.get_pressed()
        self.movement_vector = array([0, 0], dtype='f')

        if self.state == "GAME":
            y_movement = False
            for control_key in Controls.MOVEMENT:
                if keys[control_key]:
                    if control_key == pygame.K_w:
                        y_movement = True
                    
                    self.movement_vector += Controls.MOVEMENT_VECTORS[control_key]

            self.movement_vector *= Config.MOVEMENT_SPEED
            self.player.move(self.movement_vector)

    def draw(self):
        self.clock.tick(Config.FPS) # changes with the FPS in config.py

        if self.state == "START":
            self.start.update()
            self.state = self.start.state
            if self.state == "GAME":
                self.reset_game()
        elif self.state == "GAME":
            self.tilemap.update()
            self.code_runner.update()
            self.menu_button = TextButton(self.screen, position=(self.screen.get_size()[0] - 10 - 100, 10), size=(100, 50), text="Menu", bg_colour=(40, 40, 40), fg_colour=(192,192,192))
        

        
        


if __name__ == "__main__":
    game = Game()  