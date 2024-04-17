# menu.py

import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen # Récupérer l'écran du jeu 1080x720
        self.is_visible = True
        self.buttons = [ 
            {
                'text': 'Reprendre',
                'rect': pygame.Rect(390, 225, 300, 50)
            },
            {
                'text': 'Quitter',
                # 'icon': pygame.image.load('assets/exit.png'),  # Charger l'icône 
                'rect': pygame.Rect(390, 375, 300, 50)
            }
        ]
        self.font = pygame.font.Font(None, 36)


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
        

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Bouton gauche de la souris
                for button in self.buttons:
                    if button['rect'].collidepoint(event.pos):
                        if button['text'] == 'Quitter':
                            pygame.quit()
                        if button['text'] == 'Reprendre':
                            self.toggle_visibility() # Fermer le menu
                            return