import pygame
from sprite_coba import *
from config_coba import *
import sys


class Credits(MENU):
    def __init__(self, bgimage):
        self.screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
        self.bg_image = bgimage
        self.bg_credit = pygame.image.load(f"{self.bg_image}")
        self.caption = pygame.display.set_caption('game base')
        self.clock = pygame.time.Clock()
        self.running = True
        self.click = False
        self.running = True
        # self.IMAGE = 'DEFAULT'

    # def set_background(self,image):
    #     self.bg_theme = pygame.image.load(f"{image}")
                                                     
    def clicks(self):
        mx, my = pygame.mouse.get_pos()


        if self.button_theme_3.rect.collidepoint((mx, my)):
            if self.click:
                # self.angka = 2
                self.running = False

    def event(self):
        self.clicks()
        self.click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True
                   
    def new(self):
        self.all_sprites_theme = pygame.sprite.LayeredUpdates()
        self.button_theme_3 = theme3(self, 420, 560)
        
    def draw(self):
        self.screen.blit(self.bg_credit, (0,0))
        self.all_sprites_theme.draw(self.screen)
        # self.all_sprites_theme.empty()
        pygame.display.update()

    def update(self):
        self.all_sprites_theme.update()

    def main(self):
        while self.running:
            self.new()
            self.event()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        self.running = False
        return