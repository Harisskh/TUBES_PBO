import pygame

pygame.font.init()
class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, cls, x, y, groups, layer):
        self.cls = cls
        self._layer = layer
        self.groups = groups
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.image = pygame.Surface((0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class ScoreText(BaseSprite):
    def __init__(self, cls, x, y, text, groups, layer=4, font_size=80):
        super().__init__(cls, x, y, groups, layer)
        self.text = text
        self.font_size = font_size
        self.font = pygame.font.Font(None, self.font_size)  # None uses the default font
        self.update_text(self.text)

    def update_text(self, new_text):
        self.text = new_text
        self.image = self.font.render(self.text, True, (255, 255, 255))  # Render text with white color
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        # This can be used to update the text dynamically if needed
        pass

# Contoh penggunaan
pygame.init()
screen = pygame.display.set_mode((800, 600))
all_sprites = pygame.sprite.LayeredUpdates()
score_text = ScoreText(None, 100, 50, 'Score: 0', all_sprites)

running = True
score = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    score_text.update_text(f'{score}')
    
    all_sprites.update()
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    # pygame.time.wait(1000)  # Update the score every second for demonstration

pygame.quit()
