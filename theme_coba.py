import pygame
from sprite_coba import *
from config_coba import *
import sys

class Themes(MENU):
    def __init__(self, bgimage):
        self.screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
        self.bg_image = bgimage
        # self.bg_image = "asset/background/Themes.png"
        self.bg_theme = pygame.image.load(f"{self.bg_image}")
        self.caption = pygame.display.set_caption('game base')
        self.clock = pygame.time.Clock()
        self.running = True
        self.click = False
        self.running = True
        self.IMAGE = 'DEFAULT'

    def set_background(self,image):
        self.bg_theme = pygame.image.load(f"{image}")
                                                     
    def clicks(self):
        mx, my = pygame.mouse.get_pos()

        if self.object_thema1_button.rect.collidepoint((mx, my)):
            self.object_thema1_image.ops = 200
            if self.click:
                self.object_thema1_image.ops = 255
                self.IMAGE = 'PIXEL'
        
        if self.object_thema2_button.rect.collidepoint((mx, my)):
            self.object_thema2_image.ops = 200
            if self.click:
                self.IMAGE = 'NEON'
                self.object_thema2_image.ops = 255

        if self.object_ok_button.rect.collidepoint((mx, my)):
            self.object_ok_image.ops = 200
            if self.click:
                self.object_ok_image.ops = 255
                self.running = False

        if self.IMAGE == 'NEON':
            self.object_thema2_image.ops = 150
        elif self.IMAGE == 'PIXEL':
            self.object_thema1_image.ops = 150



        
        # if self.button_theme_2.rect.collidepoint((mx, my)):
        #     if self.click:
        #         self.IMAGE = 'PIXEL'
        #         # self.bg_image = "asset/background/Pixel_Game.png"
        #         # self.set_background(self.bg_image)

        # if self.button_theme_3.rect.collidepoint((mx, my)):
        #     if self.click:
        #         # self.angka = 2
        #         self.running = False

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
        self.object_thema1_image = ImageBoardTheme(self, 238,230, "asset/object/Theme_Pixel.png",1)
        self.object_thema2_image = ImageBoardTheme(self, 528,230, "asset/object/Theme_Neon.png",1)
        self.object_thema1_button = ThemeBoard(self, 238,230)
        self.object_thema2_button = ThemeBoard(self, 528,230)
        self.object_ok_button = OKBoardTheme(self, 380.3,400)
        self.object_ok_image = ImageBoardTheme(self, 360,395, "asset/object/OK.png",1)

        
    def draw(self):
        self.screen.blit(self.bg_theme, (0,0))
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
        return self.IMAGE

# th = Themes("asset/background/Themes.png")

# angka = th.main()

# print(f"{angka}")





