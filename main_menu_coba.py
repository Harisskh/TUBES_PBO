import pygame
from sprite_coba import *
from config_coba import *
from Tictactoe_coba import Tictactoe
from theme_coba import *
from menu_credit import *
from object import Object
from menu_settings import Setting
import sys

class Main(MENU):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
        self.caption = pygame.display.set_caption('game menu')
        self.clock = pygame.time.Clock()
        self.running = True
        self.click = False
        self.running = True
        self.pilih_object_1 = '0'
        self.pilih_object_2 = '0'
        self.bg_thema = "asset/background/Themes.png"
        self.bg_tictactoe = "asset/background/game_bg.png"
        self.bg_main_menu = "asset/background/Neon_Intro.png"
        self.bg_credit = "asset/background/Credits.png"
        self.bg_object = "asset/object/Object2.png"
        self.bg_setting = "asset/background/Settings.png"
        self.bg_intro = pygame.image.load(f"{self.bg_main_menu}")
        self.pilih_tema = 'NEON'
        self.apapun = ""

    def clicks(self):
        mx, my = pygame.mouse.get_pos()
        if self.button_start.rect.collidepoint((mx, my)):
            if self.click:
                self.game()

        if self.button_object.rect.collidepoint((mx, my)):
            if self.click:
                self.object()     

        if self.button_theme.rect.collidepoint((mx, my)):
            if self.click:
                self.theme()
        if self.button_credit.rect.collidepoint((mx, my)):
            if self.click:
                self.credit()

        if self.button_setting.rect.collidepoint((mx, my)):
            if self.click:
                self.setting()

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
        self.all_sprites_main_menu = pygame.sprite.LayeredUpdates()
        if self.pilih_tema == 'NEON':
            self.button_start = Main_Menu_START(self, 385, 388.5)
            self.button_theme = Main_Menu_THEME(self, 280, 585)
            self.button_credit = Main_Menu_Credit(self, 725,585 )
            self.button_object = Main_Menu_Object(self, 502.5,550)
            self.button_setting = Main_Menu_Setting(self, 53.5,550)
        elif self.pilih_tema == 'PIXEL':
            self.button_start = Main_Menu_START(self, 385, 380)
            self.button_theme = Main_Menu_THEME(self, 285, 580)
            self.button_credit = Main_Menu_Credit(self, 730,580)
            self.button_object = Main_Menu_Object(self, 502.5,550)
            self.button_setting = Main_Menu_Setting(self, 53.5,550)
        else :
            self.button_start = Main_Menu_START(self, 385, 388.5)
            self.button_theme = Main_Menu_THEME(self, 280, 585)
            self.button_credit = Main_Menu_Credit(self, 725,585 )
            self.button_object = Main_Menu_Object(self, 502.5,550)
            self.button_setting = Main_Menu_Setting(self, 53.5,550)

    def draw(self):
        self.screen.blit(self.bg_intro, (0,0))
        self.all_sprites_main_menu.draw(self.screen)
        self.all_sprites_main_menu.empty()
        pygame.display.update()

    def update(self):
        self.all_sprites_main_menu.update()

    def main(self):
        try:
            while self.running:
                print(f"{self.pilih_object_1, self.pilih_object_2}")
                self.new()
                self.event()
                self.update()
                self.draw()
                self.clock.tick(FPS)
            self.running = False
        except Exception as e:
            print(f"Error pada menu main menu: {e}")
        
    def game(self):
        tt = Tictactoe(self.pilih_tema, self.pilih_object_1, self.pilih_object_2)
        self.apapun = tt.main()
        print(f"{self.apapun}")

    def theme(self):
        th = Themes(self.bg_thema)
        self.pilih_tema = th.main()
        print(f"{self.pilih_tema}")
        if self.pilih_tema == 'NEON':
            self.bg_thema = "asset/background/Themes.png"
            self.bg_tictactoe = "asset/background/game_bg.png"
            self.bg_main_menu = "asset/background/Neon_Intro.png"
            self.bg_intro = pygame.image.load(f"{self.bg_main_menu}")
            # print(f"{self.pilih_tema}")

        if self.pilih_tema == 'PIXEL':
            self.bg_thema = "asset/background/Themes.png"
            self.bg_tictactoe = "asset/background/Pixel.png"
            self.bg_main_menu = "asset/background/Pixel.png"
            self.bg_intro = pygame.image.load(f"{self.bg_main_menu}")
            # print(f"{self.pilih_tema}")

    def credit(self):
        cr = Credits(self.bg_credit)
        cr.main()

    def object(self):
        o = Object(self.bg_object, self.pilih_tema)
        self.pilih_object_1, self.pilih_object_2 = o.main()

    def setting(self):
        st = Setting(self.bg_setting)
        st.main()

g = Main()
g.main()

