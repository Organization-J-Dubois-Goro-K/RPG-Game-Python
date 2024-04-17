# bottom_interface.py

import pygame

class BottomInterface:
    def __init__(self, screen):
        self.screen = screen
        self.is_fighting = False # Lorsque le joueur est en combat, afficher l'interface de combat
        self.buttons = [
            {
                'icon': pygame.image.load('assets/menu_close.png'),  # Charger l'icône du menu
                'rect': pygame.Rect(1000, 630, 80, 80)  # Positionner le bouton
            },
        ]
    
    def draw(self):
        pygame.draw.rect(self.screen, (150, 150, 150), (0, 620, 1080, 100), 0)
        for button in self.buttons:
            self.screen.blit(button['icon'], (button['rect'].x, button['rect'].y))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for button in self.buttons:
                    if button['icon'].get_rect(topleft=(0, 620)).collidepoint(event.pos):
                        print('Menu button clicked')
                        return