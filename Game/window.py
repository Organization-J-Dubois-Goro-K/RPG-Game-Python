import pygame
pygame.init()


#Set up the drawing window
screen = pygame.display.set_mode([500, 500])


#Run until the user asks to quit
running = True
while running:

    # Did the user click the window close the button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the backgound with white
    screen.fill((255,255,255))
    screen.

    # Draw a solid blue circle int the center
    pygame.draw.circle(screen, (0,0,255),(250,250),75)

    # Flip the display (for white background)
    pygame.display.flip()

# Done Time to quit!
pygame.quit