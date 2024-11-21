import pygame
import time
from collections import deque
from config import Config

from threading import Thread
from gui.input_box import InputBox

class CodeRunner:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)

        self.custom_globals = globals().copy()

        self.custom_globals['print'] = self.custom_print
        self.custom_globals['input'] = self.custom_input

        self.print_queue = deque()

        self.input_box = None
        self.typing = False
        

    def custom_print(self, text):
        print("custom print: " + text)
        self.print_queue.append({'text': text, 'timestamp': pygame.time.get_ticks()})
    
    def custom_input(self, data):
        self.input_box = InputBox(self.screen, (100,100), (300, 50))

    def update(self):
        if self.input_box:
            self.input_box.update()
            self.typing = self.input_box.active

        print_queue_copy = self.print_queue.copy()
        for i, item in enumerate(print_queue_copy):
            if pygame.time.get_ticks() - Config.PRINT_TIMEOUT > item['timestamp']:
                self.print_queue.popleft()
            else:
                text = self.font.render(item['text'], True, (0, 0, 0))
                self.screen.blit(text, (0, i*50))

    def custom_exec(self, code):
        exec(code, self.custom_globals)

    def run_user_code(self, code):
        #exec(code, self.custom_globals)
        thread = Thread(target=self.custom_exec, args=(code, ))
        thread.start()

        

       



  
