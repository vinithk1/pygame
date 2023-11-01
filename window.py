import pygame

# Initialise pygame
pygame.init()

# Screen width and hieght
(width, height) = (300,200)

# Initialise the display 
gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pygame Window Example")

# Event handling loop 
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Close pygame after loop exit
pygame.quit()
