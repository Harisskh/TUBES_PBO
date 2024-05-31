import pygame
import sys

# Definisikan warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definisikan ukuran layar dan FPS
WIDTH, HEIGHT = 800, 600
FPS = 60

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image_normal = pygame.Surface((width, height))
        self.image_normal.fill(WHITE)
        self.image_hover = pygame.Surface((width, height))
        self.image_hover.fill(WHITE)
        self.image = self.image_normal
        self.rect = self.image.get_rect(topleft=(x, y))
        self.alpha = 255  # Opasitas awal
        self.alpha_speed = 31  # Kecepatan perubahan opasitas
        self.hovered = False

    def update(self):
        # Cek apakah posisi mouse berada di atas tombol
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hovered = True
            if self.alpha > 100:
                self.alpha -= self.alpha_speed
                print(self.alpha)
            
            if self.alpha < 100:
                self.alpha = 100
        else:
            self.hovered = False
            if self.alpha < 255:
                self.alpha += self.alpha_speed
                print(self.alpha)
        
        # Atur opasitas gambar sesuai nilai alpha
        if self.hovered:
            self.image = self.image_hover.copy()
        else:
            self.image = self.image_normal.copy()
        self.image.set_alpha(self.alpha)

# Inisialisasi pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Buat tombol
button = Button(100, 100, 200, 50)
all_sprites = pygame.sprite.Group(button)

# Perulangan utama
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

    # Tunggu hingga interval FPS
    clock.tick(FPS)

pygame.quit()
sys.exit()
