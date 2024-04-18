# menu.py

import pygame
class Menu:
    def __init__(self, screen):
        self.bottom_interface = None # Initialiser sans référence pour éviter l'erreur d'initialisation
        self.screen = screen # Récupérer l'écran du jeu 1080x720
        self.is_visible = False
        self.buttons = [ 
            {
                'text': 'Reprendre',
                'rect': pygame.Rect(390, 225, 300, 65)
            },
            {
                'text': 'Quitter',
                # 'icon': pygame.image.load('assets/exit.png'),  # Charger l'icône 
                'rect': pygame.Rect(390, 375, 300, 65)
            }
        ]
        self.font = pygame.font.Font('assets/blackjack-webfont.woff', 32)  # Charger la police de caractères

    def set_bottom_interface(self, bottom_interface):
        self.bottom_interface = bottom_interface  # Définir la référence après la création

    def draw(self):
        if self.is_visible: # Si le menu est visible, dessiner le menu
            pygame.draw.rect(self.screen,(150, 150, 150), (300, 150, 480, 400), 0, 15) # dessine le fond du menu
            for button in self.buttons:
                pygame.draw.rect(self.screen, (255, 0 , 0), button['rect'], 0, 5)  # Dessiner le bouton
                # self.screen.blit(button['icon'], (button['rect'].x + 5, button['rect'].y + 5))  # Dessiner l'icône
                text = self.font.render(button['text'], True, (255, 255, 255))  # Dessiner le texte

                if button['text'] == 'Quitter': # Positionne le texte 'Quitter' (largeur différente selon le texte) (105 et 90)
                    self.screen.blit(text, (button['rect'].x + 105, button['rect'].y + 10)) 
                if button['text'] == 'Reprendre':
                    self.screen.blit(text, (button['rect'].x + 90, button['rect'].y + 10))

    def toggle_visibility(self):
        self.is_visible = not self.is_visible # Inverser la visibilité du menu
        
    def change_icon_bottom_interface(self):
        for button in self.buttons:
            if button['text'] == 'Reprendre':
                self.bottom_interface.buttons[0]['icon'] = pygame.image.load('assets/menu_close.png')
                self.bottom_interface.buttons[0]['can_click'] = True

    def handle_event(self, event):
        if self.is_visible: # Si le menu est visible, gérer les événements
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Bouton gauche de la souris
                    for button in self.buttons:
                        if button['rect'].collidepoint(event.pos):
                            if button['text'] == 'Quitter':
                                pygame.quit()
                            if button['text'] == 'Reprendre':
                                self.toggle_visibility() # Fermer le menu
                                self.change_icon_bottom_interface() # change l'icone du menu
                                return