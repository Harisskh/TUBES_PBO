import pygame
from config_coba import *
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

    def update(self):
        pass  

class Board(BaseSprite):
    def __init__(self, cls, x, y):
        super().__init__(cls, x, y, cls.all_sprites_tictactoe, BOARD_LAYER)
        self.width = TILESIZE
        self.height = TILESIZE
        image = pygame.image.load("asset/board/Board(1).png")
        self.image = pygame.Surface([self.width, self.height])
        self.image.blit(image, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        #hover
        self.image_hover = pygame.Surface([self.width, self.height])
        self.image_hover.blit(image, (0, 0))
        self.image_hover.set_colorkey(BLACK)
        self.alpha = 255  # Opasitas awal
        self.alpha_speed = 38.75  # Kecepatan perubahan opasitas
        self.hovered = False

    def update(self):
    # Cek apakah posisi mouse berada di atas tombol
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hovered = True
            if self.alpha > 100:
                self.alpha -= self.alpha_speed
        else:
            self.hovered = False
            if self.alpha < 255:
                self.alpha += self.alpha_speed
        # Atur opasitas gambar sesuai nilai alpha
        if self.hovered:
            self.image = self.image_hover.copy()
        else:
            self.image = self.image.copy()
        self.image.set_alpha(self.alpha)



class Board(BaseSprite):
    def __init__(self, cls, x, y, imagex):
        super().__init__(cls, x, y, cls.all_sprites_tictactoe, BOARD_LAYER)
        self.width = TILESIZE
        self.height = TILESIZE
        image = pygame.image.load(imagex)
        image = pygame.transform.scale(image, (self.width, self.height))

        self.image_normal = pygame.Surface([self.width, self.height])
        self.image_normal.blit(image, (0, 0))
        self.image_normal.set_colorkey(BLACK)
        
        self.image_hover = pygame.Surface([self.width, self.height])
        self.image_hover.blit(image, (0, 0))
        self.image_hover.set_colorkey(BLACK)

        self.image = self.image_normal
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.alpha = 255  # Opasitas awal
        self.alpha_speed = 38.75  # Kecepatan perubahan opasitas
        self.hovered = None

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and self.hovered == True :
            # self.hovered = True
            if self.alpha > 150:
                self.alpha -= self.alpha_speed
        else:
            self.hovered = False
            if self.alpha < 255:
                self.alpha += self.alpha_speed

        if self.hovered:
            self.image = self.image_hover.copy()
        else:
            self.image = self.image_normal.copy()
        self.image.set_alpha(self.alpha)
    def cek_click(self, event):
        # Cek apakah tombol ditekan saat mouse di atasnya
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                # Lakukan sesuatu saat tombol ditekan
                self.alpha = 255
                self.image.set_alpha(self.alpha)
                print(f"Tombol setting diklik {self.alpha}")
                
class GameButton(BaseSprite):
    def __init__(self, cls, x, y,imagex):
        super().__init__(cls, x, y, cls.all_sprites_tictactoe, GAMEBUTTONLAYER)
        self.width = TILESIZE - 60
        self.height = TILESIZE - 60
        self._layer = GAMEBUTTONLAYER
        image = pygame.image.load(imagex)
        image_scaled = pygame.transform.smoothscale(image, (self.width, self.height))
        self.image = pygame.Surface([self.width, self.height])
        self.image.blit(image_scaled, (0, 0))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        #hover
        self.image_hover = pygame.Surface([self.width, self.height])
        self.image_hover.blit(image_scaled, (0, 0))
        self.image_hover.set_colorkey(BLACK)
        self.alpha = 255  # Opasitas awal
        self.alpha_speed = 38.75  # Kecepatan perubahan opasitas
        self.hovered = False

    def update(self):
    # Cek apakah posisi mouse berada di atas tombol
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hovered = True
            if self.alpha > 150:
                self.alpha -= self.alpha_speed
        else:
            self.hovered = False
            if self.alpha < 255:
                self.alpha += self.alpha_speed
        # Atur opasitas gambar sesuai nilai alpha
        if self.hovered:
            self.image = self.image_hover.copy()
        else:
            self.image = self.image.copy()
        self.image.set_alpha(self.alpha)

    def set_alpha(self,alpha):
        if self.alpha != 255:
            self.image.set_alpha(alpha)
        else :
            self.alpha = 210

class XButton(BaseSprite):
    def __init__(self, cls, x, y,imagex):
        super().__init__(cls, x, y, cls.all_sprites_tictactoe, 13)
        self.width = TILESIZE - 90
        self.height = TILESIZE - 90
        image = pygame.image.load(imagex)
        image_scaled = pygame.transform.smoothscale(image, (self.width, self.height))
        self.image = pygame.Surface([self.width, self.height])
        self.image.blit(image_scaled, (0, 0))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        #hover
        self.image_hover = pygame.Surface([self.width, self.height])
        self.image_hover.blit(image_scaled, (0, 0))
        self.image_hover.set_colorkey(BLACK)
        self.alpha = 255  # Opasitas awal
        self.alpha_speed = 38.75  # Kecepatan perubahan opasitas
        self.hovered = False

    def update(self):
    # Cek apakah posisi mouse berada di atas tombol
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hovered = True
            if self.alpha > 150:
                self.alpha -= self.alpha_speed
        else:
            self.hovered = False
            if self.alpha < 255:
                self.alpha += self.alpha_speed
        # Atur opasitas gambar sesuai nilai alpha
        if self.hovered:
            self.image = self.image_hover.copy()
        else:
            self.image = self.image.copy()
        self.image.set_alpha(self.alpha)

    def set_alpha(self,alpha):
        if self.alpha != 255:
            self.image.set_alpha(alpha)
        else :
            self.alpha = 210
  
class InputBoard(BaseSprite):
    def __init__(self, cls, x, y):
        super().__init__(cls, x, y, cls.all_sprites_tictactoe, INPUT_BOARD_LAYER)
        self.width = TILESIZE
        self.height = TILESIZE
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
            
class Player1_Board(BaseSprite):
    def __init__(self, cls, x, y, image):
        super().__init__(cls, x, y, cls.all_sprites_tictactoe, INPUT_BOARD_X_LAYER)
        self.width = TILESIZE
        self.height = TILESIZE
        image = pygame.image.load(image)
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey(BLACK)
        self.image.blit(image, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Player2_Board(BaseSprite):
    def __init__(self, cls, x, y,image):
        super().__init__(cls, x, y, cls.all_sprites_tictactoe, INPUT_BOARD_Y_LAYER)
        self.width = TILESIZE
        self.height = TILESIZE
        image = pygame.image.load(image)
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey(BLACK)
        self.image.blit(image, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.alpha = 255

class Main_Menu_START(BaseSprite):
    def __init__(self, cls, x, y):
        super().__init__(cls, x, y, cls.all_sprites_main_menu, LAYER)
        self.width = 208
        self.height = 60
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)
        self.image.set_colorkey(RED)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Main_Menu_THEME(BaseSprite):
    def __init__(self, cls, x, y):
        super().__init__(cls, x, y, cls.all_sprites_main_menu, LAYER)
        self.width = 208
        self.height = 60
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)
        self.image.set_colorkey(RED)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Main_Menu_Credit(BaseSprite):
    def __init__(self, cls, x, y):
        super().__init__(cls, x, y, cls.all_sprites_main_menu, LAYER)
        self.width = 208
        self.height = 60
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)
        self.image.set_colorkey(RED)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Main_Menu_Object(BaseSprite):
    def __init__(self, cls, x, y):
        super().__init__(cls, x, y, cls.all_sprites_main_menu, LAYER)
        self.width = 208
        self.height = 58.5
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)
        self.image.set_colorkey(RED)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Main_Menu_Setting(BaseSprite):
    def __init__(self, cls, x, y):
        super().__init__(cls, x, y, cls.all_sprites_main_menu, LAYER)
        self.width = 208
        self.height = 58.5
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)
        self.image.set_colorkey(RED)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class ThemeBase(BaseSprite):
    def __init__(self, cls, x, y, groups, layer):
        super().__init__(cls, x, y, groups, layer)
        self.width = 208
        self.height = 70
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)
        self.image.set_colorkey(RED)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class theme1(ThemeBase):
    def __init__(self, cls, x, y):
        super().__init__(cls, x, y, cls.all_sprites_theme, LAYER)

class theme2(ThemeBase):
    def __init__(self, cls, x, y):
        super().__init__(cls, x, y, cls.all_sprites_theme, LAYER)

class theme3(ThemeBase):
    def __init__(self, cls, x, y):
        super().__init__(cls, x, y, cls.all_sprites_theme, LAYER)


class ScoreText(BaseSprite):
    def __init__(self, cls, x, y, text, warna, layer=4, font_size=140):
        super().__init__(cls, x, y, cls.all_sprites_tictactoe, layer)
        self.text = str(text)  # Ensure text is a string
        self.font_size = font_size
        self.warna = warna
        self.font = pygame.font.Font(None, self.font_size)  # None uses the default font
        self.update_text(self.text, self.warna)

    def update_text(self, new_text, warna):
        self.text = str(new_text)  # Ensure text is a string
        self.font_colour = warna
        self.image = self.font.render(f"{self.text}", True, self.font_colour)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)  # Set position of the rect

    def update(self):
        # This can be used to update the text dynamically if needed
        pass

class TimerText(BaseSprite):
    def __init__(self, cls, x, y, text, warna, layer=5, font_size=60):
        super().__init__(cls, x, y, cls.all_sprites_tictactoe, layer)
        self.text = str(text)  # Ensure text is a string
        self.font_size = font_size
        self.warna = warna
        self.font = pygame.font.Font('asset/font/ArialRoundedMTBold.ttf', self.font_size)  # None uses the default font
        self.update_text(self.text, self.warna)

    def update_text(self, new_text, warna):
        if int(new_text) < 0 :
            new_text = 0
        self.text = str(new_text).zfill(2)  # Ensure text is a string
        self.font_colour = warna
        self.image = self.font.render(f"{self.text:02}", True, self.font_colour)  # Render text with white color
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)  # Set position of the rect

    def update(self):
        # This can be used to update the text dynamically if needed
        pass

class TimerBoard(BaseSprite):
    def __init__(self, cls, x, y):
        super().__init__(cls, x, y, cls.all_sprites_tictactoe, 4)
        self.width = 240
        self.height = 70
        self.image = pygame.image.load("asset/board/Neon_Timer.png")




class ImageBoard(BaseSprite):
    def __init__(self, cls, x, y,image,layer):
        super().__init__(cls, x, y, cls.all_sprites_tictactoe, layer)
        self.image = pygame.image.load(image)

class HelpBoard(BaseSprite):
    def __init__(self, cls, x, y,image):
        super().__init__(cls, x, y, cls.all_sprites_tictactoe, 11)
        self.width = 400
        self.height = 70
        self.image = pygame.image.load(image)

class ObjectBoard(BaseSprite):
    def __init__(self, cls, x, y):
        super().__init__(cls, x, y, cls.all_sprites_object, INPUT_BOARD_Y_LAYER)
        self.width = 100
        self.height = 100
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.alpha = 255

class OKBoard(BaseSprite):
    def __init__(self, cls, x, y):
        super().__init__(cls, x, y, cls.all_sprites_object , 1)
        self.width = 215
        self.height = 65
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class ImageBoardObject(BaseSprite):
    def __init__(self, cls, x, y, image):
        super().__init__(cls, x, y, cls.all_sprites_object, 0)
        self.image = pygame.image.load(image).convert_alpha()
        self._ops = 255
        self.update_alpha()

    @property
    def ops(self):
        return self._ops
    
    @ops.setter
    def ops(self, opasitas):
        self._ops = opasitas
        self.update_alpha()

    def update_alpha(self):
        # Mengatur alpha pada gambar
        self.image.set_alpha(self._ops)

class ModeBoard(BaseSprite):
    def __init__(self, cls, x, y, layer):
        super().__init__(cls, x, y, cls.all_sprites_tictactoe, layer)
        self.width = 180
        self.height = 50
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)
        self.image.set_colorkey(RED)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.alpha = 255

class OKBoardTheme(BaseSprite):
    def __init__(self, cls, x, y):
        super().__init__(cls, x, y, cls.all_sprites_theme , 2)
        self.width = 215
        self.height = 65
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class ImageBoardTictactoe(BaseSprite):
    def __init__(self, cls, x, y, image, layer):
        super().__init__(cls, x, y, cls.all_sprites_tictactoe, IMAGE_LAYER)
        self.x = x
        self.y = y
        self.image = pygame.image.load(image).convert_alpha()
        self._ops = 255
        self.update_alpha()

    @property
    def ops(self):
        return self._ops
    
    @ops.setter
    def ops(self, opasitas):
        self._ops = opasitas
        self.update_alpha()

    def update_alpha(self):
        # Mengatur alpha pada gambar
        self.image.set_alpha(self._ops)

class ThemeBoard(BaseSprite):
    def __init__(self, cls, x, y):
        super().__init__(cls, x, y, cls.all_sprites_theme, INPUT_BOARD_Y_LAYER)
        self.width = 210
        self.height = 150
        self.image = pygame.Surface([self.width, self.height])
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.alpha = 255

class ImageBoardTheme(BaseSprite):
    def __init__(self, cls, x, y, image, layer):
        super().__init__(cls, x, y, cls.all_sprites_theme, IMAGE_LAYER)
        self.x = x
        self.y = y
        self.image = pygame.image.load(image).convert_alpha()
        self._ops = 255
        self.update_alpha()

    @property
    def ops(self):
        return self._ops
    
    @ops.setter
    def ops(self, opasitas):
        self._ops = opasitas
        self.update_alpha()

    def update_alpha(self):
        # Mengatur alpha pada gambar
        self.image.set_alpha(self._ops)

class OKBoardSetting(BaseSprite):
    def __init__(self, cls, x, y):
        super().__init__(cls, x, y, cls.all_sprites_setting , 2)
        self.width = 215
        self.height = 65
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class SettingBoard(BaseSprite):
    def __init__(self, cls, x, y):
        super().__init__(cls, x, y, cls.all_sprites_setting, INPUT_BOARD_Y_LAYER)
        self.width = 50
        self.height = 50
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.alpha = 255

class ImageBoardSetting(BaseSprite):
    def __init__(self, cls, x, y, image, layer):
        super().__init__(cls, x, y, cls.all_sprites_setting, IMAGE_LAYER)
        self.x = x
        self.y = y
        self.image = pygame.image.load(image).convert_alpha()
        self._ops = 255
        self.update_alpha()

    @property
    def ops(self):
        return self._ops
    
    @ops.setter
    def ops(self, opasitas):
        self._ops = opasitas
        self.update_alpha()

    def update_alpha(self):
        # Mengatur alpha pada gambar
        self.image.set_alpha(self._ops)
