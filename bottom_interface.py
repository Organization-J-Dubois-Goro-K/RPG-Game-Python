# bottom_interface.py

import pygame

class BottomInterface:
    def __init__(self, screen):
        self.menu = None
        self.screen = screen
        self.is_fighting = False # Lorsque le joueur est en combat, afficher l'interface de combat
        self.buttons = [
            {
                'icon': pygame.image.load('assets/menu_close.png'),  # Charger l'icône du menu
                'rect': pygame.Rect(1000, 630, 80, 80),  # Positionner le bouton
                'title': 'Menu',
                'can_click' : True
            },
        ]

    def set_menu(self, menu):
        self.menu = menu
    
    def draw(self):
        pygame.draw.rect(self.screen, (150, 150, 150), (0, 620, 1080, 100), 0)
        for button in self.buttons:
            self.screen.blit(button['icon'], (button['rect'].x, button['rect'].y))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for button in self.buttons:
                    if button['rect'].collidepoint(event.pos) and button['title'] == 'Menu' and button['can_click'] == True: # Si le bouton du menu est cliqué alors ouvre le menu
                        button['icon'] = pygame.image.load('assets/menu_open.png') # Change l'icône du menu
                        self.menu.toggle_visibility() # rend visible le menu
                        button['can_click'] = False
                    

                    