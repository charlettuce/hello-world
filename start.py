import pygame
from config import Config

from gui.text_button import TextButton
from gui.text_image_button import TextImageButton

class StartMenu:
    def __init__(self, screen):
        self.state = "START"
        self.start_state = "MAIN"
        self.screen = screen
        self.selected_character = Config.DEFAULT_CHARACTER

        self.scene_change()

    
    def scene_change(self):
        self.screen.fill((65,65,65))
        if self.start_state == "MAIN":
            pygame.display.set_caption("Start Menu")
            self.start_button = TextButton(self.screen, position=(150, 50), size=(200, 100), text="Start Game", bg_colour=(40, 40, 40), fg_colour=(192,192,192))  
            self.character_select_button = TextButton(self.screen, position=(150, 200), size=(200, 100), text="Character Select", bg_colour=(40, 40, 40), fg_colour=(192,192,192))
            self.quit_button = TextButton(self.screen, position=(150, 350), size=(200, 100), text="Quit Game", bg_colour=(40, 40, 40), fg_colour=(192,192,192))
        elif self.start_state == "CHARACTER_SELECT":
            pygame.display.set_caption("Character Select")

            self.back_button = TextButton(self.screen, position=(10, 10), size=(100, 50), text="Back", bg_colour=(40, 40, 40), fg_colour=(192,192,192))
            self.select_character_buttons = [TextImageButton(self.screen, position=((i+1)*self.screen.get_size()[0]/5, 150), size=(150, 300), text=("Character " + str(i+1)), bg_colour=(40, 40, 40), fg_colour=(192,192,192), image_path="assets/player/player_" + str(i+1) + ".png") for i in range(Config.NUMBER_OF_CHARACTERS)]

    def update(self):
        self.scene_change()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            elif event.type == pygame.VIDEORESIZE:
                self.scene_change()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_state == "MAIN":
                    if self.start_button.collidepoint(event.pos):
                        self.state = "GAME"
                    if self.character_select_button.collidepoint(event.pos):
                        self.start_state = "CHARACTER_SELECT"
                        self.scene_change()
                    elif self.quit_button.collidepoint(event.pos):
                        pygame.quit()
                        exit()
                elif self.start_state == "CHARACTER_SELECT":
                    if self.back_button.collidepoint(event.pos):
                        self.start_state = "MAIN"
                        self.scene_change()
                    for i, button in enumerate(self.select_character_buttons):
                        if button.collidepoint(event.pos):
                            self.selected_character = i
                            self.scene_change()