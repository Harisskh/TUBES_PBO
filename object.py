import pygame
from sprite_coba import *
from config_coba import *
import sys



class Object(MENU):
    def __init__(self, bgimage = "asset/object/Object2.png", imagex = 'NEON', object1 = 0, object2 = 0):
        self.screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
        self.bg_image = bgimage
        self.object1 = object1
        self.object2 = object2
        self.bg_theme = pygame.image.load(f"{self.bg_image}")
        self.caption = pygame.display.set_caption('game base')
        self.clock = pygame.time.Clock()
        self.running = True
        self.click = False
        self.running = True
        self.IMAGE = imagex
        # self.alpha_image_choice = 0
        self.choice_1 = '0'
        self.choice_2 = '0'
        self.object_X_image = "asset/object/Object_Cs.png"

    def set_background(self,image):
        self.bg_theme = pygame.image.load(f"{image}")
                                                     
    def clicks(self):
        mx, my = pygame.mouse.get_pos()

        if self.object_ok_button.rect.collidepoint((mx, my)):
            self.object_ok_image.ops = 200
            if self.click:
                self.object_ok_image.ops = 255
                self.running = False
                # self.choice = '1'

        if self.object_x_button.rect.collidepoint((mx, my)):
            self.object_x_image.ops = 200
            if self.click:
                self.object_x_image.ops = 255
                self.choice_1 = '1'
        
        if self.object_tr_button.rect.collidepoint((mx, my)):
            self.object_tr_image.ops = 200
            if self.click:
                self.object_tr_image.ops = 255
                self.choice_1 = '2'
        
        if self.object_o_button.rect.collidepoint((mx, my)):
            self.object_o_image.ops = 200
            if self.click:
                self.object_o_image.ops = 255
                self.choice_2 = '1'

        if self.object_sq_button.rect.collidepoint((mx, my)):
            self.object_sq_image.ops = 200
            if self.click:
                self.object_sq_image.ops = 255
                self.choice_2 = '2'

                

        if self.choice_1 == '1':
            self.object_x_image.ops = 150
        elif self.choice_1 == '2':
            self.object_tr_image.ops = 150

        if self.choice_2 == '1':
            self.object_o_image.ops = 150
        elif self.choice_2 == '2':
            self.object_sq_image.ops = 150
                # self.running = False
        
        # if self.choice == '1':
        #     self.object_ok_image.ops = 150

                

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
        self.all_sprites_object = pygame.sprite.LayeredUpdates()
        self.object_x_button = ObjectBoard(self, 265,205)
        self.object_tr_button = ObjectBoard(self, 265,330)
        self.object_o_button = ObjectBoard(self, 588,205)
        self.object_sq_button = ObjectBoard(self, 588,330)
        
        if self.IMAGE == 'NEON':
            self.object_x_image = ImageBoardObject(self, 265,205, "asset/object/Object_Cs.png")
            self.object_tr_image = ImageBoardObject(self, 265,330, "asset/object/Object_Tr.png")
            self.object_o_image = ImageBoardObject(self, 588,205, "asset/object/Object_Cr.png")
            self.object_sq_image = ImageBoardObject(self, 588,330, "asset/object/Object_Sq.png")
            self.object_ok_button = OKBoard(self, 380.3,450)
            self.object_ok_image = ImageBoardObject(self, 362.5,432, "asset/object/OK.png")
        elif self.IMAGE == 'PIXEL':
            self.object_x_image = ImageBoardObject(self, 265,205, "asset/button/Object_Cs_Px.png")
            self.object_tr_image = ImageBoardObject(self, 265,330, "asset/button/Object_Tr_Px.png")
            self.object_o_image = ImageBoardObject(self, 588,205, "asset/button/Object_Cr_Px.png")
            self.object_sq_image = ImageBoardObject(self, 588,330, "asset/button/Object_Sq_Px.png")
            self.object_ok_button = OKBoard(self, 380.3,450)
            self.object_ok_image = ImageBoardObject(self, 362.5,432, "asset/object/OK.png")
        else :
            self.object_x_image = ImageBoardObject(self, 265,205, "asset/object/Object_Cs.png")
            self.object_tr_image = ImageBoardObject(self, 265,330, "asset/object/Object_Tr.png")
            self.object_o_image = ImageBoardObject(self, 588,205, "asset/object/Object_Cr.png")
            self.object_sq_image = ImageBoardObject(self, 588,330, "asset/object/Object_Sq.png")
            self.object_ok_button = OKBoard(self, 380.3,450)
            self.object_ok_image = ImageBoardObject(self, 362.5,432, "asset/object/OK.png")


    def draw(self):
        self.screen.blit(self.bg_theme, (0,0))
        self.all_sprites_object.draw(self.screen)
        # self.all_sprites_theme.empty()
        # self.object_ok_image.ops = 130
        pygame.display.update()

    def update(self):
        self.all_sprites_object.update()

    def main(self):
        while self.running:
            # self.clicks()
            self.new()
            self.event()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        self.running = False
        return self.choice_1, self.choice_2

# o = Object()
# o.main()






