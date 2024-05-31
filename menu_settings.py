import pygame
from sprite_coba import *
from config_coba import *
import sys

class Setting(MENU):
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

        # if self.object_thema1_button.rect.collidepoint((mx, my)):
        #     self.object_thema1_image.ops = 200
        #     if self.click:
        #         self.object_thema1_image.ops = 255
        #         self.IMAGE = 'PIXEL'
        
        # if self.object_thema2_button.rect.collidepoint((mx, my)):
        #     self.object_thema2_image.ops = 200
        #     if self.click:
        #         self.IMAGE = 'NEON'
        #         self.object_thema2_image.ops = 255

        if self.object_ok_button.rect.collidepoint((mx, my)):
            self.object_ok_image.ops = 200
            if self.click:
                self.object_ok_image.ops = 255
                self.running = False

        # if self.IMAGE == 'NEON':
        #     self.object_thema2_image.ops = 150
        # elif self.IMAGE == 'PIXEL':
        #     self.object_thema1_image.ops = 150



        
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
        self.all_sprites_setting = pygame.sprite.LayeredUpdates()
        self.object_min1_image = ImageBoardSetting(self, 420,260, "asset/button/Music_Min_Settings.png",1)
        self.object_min2_image = ImageBoardSetting(self, 420,325, "asset/button/Music_Min_Settings.png",1)
        self.object_plus1_image = ImageBoardSetting(self, 515,260, "asset/button/Music_Plus_Settings.png",1)
        self.object_plus2_image = ImageBoardSetting(self, 515,325, "asset/button/Music_Plus_Settings.png",1)
        self.object_soundmute_image = ImageBoardSetting(self, 421, 390, "asset/button/Music_Mute_Settings.png",1)
        self.object_soundon_image = ImageBoardSetting(self, 514, 393, "asset/button/Music_Sound_Settings.png",1)
        self.object_min1_button = SettingBoard(self, 238,230)
        self.object_min2_button = SettingBoard(self, 238,280)
        self.object_plus1_button = SettingBoard(self, 238,230)
        self.object_plus2_button = SettingBoard(self, 238,230)
        self.object_soundmute_button = SettingBoard(self, 238,230)
        self.object_soundon_button = SettingBoard(self, 528,230)
        self.object_ok_button = OKBoardSetting(self, 380.3,500)
        self.object_ok_image = ImageBoardSetting(self, 360,500, "asset/object/OK.png",1)

        
    def draw(self):
        self.screen.blit(self.bg_theme, (0,0))
        self.all_sprites_setting.draw(self.screen)
        # self.all_sprites_theme.empty()
        pygame.display.update()

    def update(self):
        self.all_sprites_setting.update()

    def main(self):
        while self.running:
            self.new()
            self.event()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        self.running = False
        return self.IMAGE

# st = Setting("asset/background/Settings.png")

# angka = st.main()

# print(f"{angka}")





