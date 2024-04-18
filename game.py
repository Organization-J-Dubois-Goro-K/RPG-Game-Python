# game.py
import pygame
from menu import Menu
from bottom_interface import BottomInterface

class Game:
    def __init__(self):
        pygame.init()
        # Créer la fenêtre du jeu
        self.screen = pygame.display.set_mode((1080, 720))
        
        # Créer les instances sans références croisées
        self.menu = Menu(self.screen)
        self.bottom_interface = BottomInterface(self.screen)

        # Établir les références croisées après l'initialisation
        self.menu.set_bottom_interface(self.bottom_interface)
        self.bottom_interface.set_menu(self.menu)

        pygame.display.set_caption("Rpg Game")
    
    def run(self):
        # Boucle de jeu
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.menu.handle_event(event)
                self.bottom_interface.handle_event(event)
            self.screen.fill((0, 0, 0))
            self.menu.draw()
            self.bottom_interface.draw()
            pygame.display.flip()
        pygame.quit()
