import pygame
import sys

# Initialize Pygame
pygame.init()

# Window dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Text Display")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
# You can use a system font by name, or a specific font file.
# If using a font file, ensure it's in the same directory as your script
# or provide the full path.
font1 = pygame.font.SysFont("Arial", 48)  # System font: Arial, size 48
font2 = pygame.font.Font("freesansbold.ttf", 36) # Default Pygame font or a custom .ttf file

# Text surfaces
text_surface1 = font1.render("Hello from Pygame!", True, BLACK)
text_surface2 = font2.render("Different font, different size!", True, BLACK)

# Get text rectangles for positioning
text_rect1 = text_surface1.get_rect(center=(WIDTH // 2, HEIGHT // 3))
text_rect2 = text_surface2.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    SCREEN.fill(WHITE)

    # Blit (draw) the text surfaces onto the screen
    SCREEN.blit(text_surface1, text_rect1)
    SCREEN.blit(text_surface2, text_rect2)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
