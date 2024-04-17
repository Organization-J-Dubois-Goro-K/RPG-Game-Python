# bottom_interface.py

import pygame

class BottomInterface:
    def __init__(self, screen):
        self.screen = screen
        self.is_fighting = False # Lorsque le joueur est en combat, afficher l'interface de combat
        self.buttons = [
            {
                'icon': pygame.image.load('assets/menu.png'),  # Charger l'icône du menu
            },
        ]
        