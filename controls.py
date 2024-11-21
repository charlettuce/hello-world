import pygame
from numpy import array


class Controls:
    MOVEMENT = [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s]

    MOVEMENT_VECTORS = {
        pygame.K_a: array([-1, 0]),  # Move left
        pygame.K_d: array([1, 0]),   # Move right
        pygame.K_w: array([0, -1]),  # Move up
        pygame.K_s: array([0, 1]),   # Move down
    }