import pygame
import sys
from sprite_coba import *
from config_coba import *
# pygame.init()
pygame.font.init()
class Tictactoe(MENU):
    def __init__ (self, image, o1, o2 ):
        self.screen = pygame.display.set_mode((S_WIDTH,S_HEIGHT))
        # self.IMAGE = 'NEON'
        self.IMAGE = image
        self.warna = WHITE
        # self.backsound = pygame.mixer.Sound('asset/sound/1148818_Cyberpunk (1).wav')
        self.play_sound = False
        self.score_count_1 = 0
        self.score_count_2 = 0
        self.pilih_object_1 = o1
        self.pilih_object_2 = o2
        self.mode_start_time = 1
        self.help = False
        self.clik_mode = False
        self.click_button_game = True
        self.click_button_game_x = True
        self.clock = pygame.time.Clock()
        self.init_timer = pygame.time.set_timer(pygame.USEREVENT,1000)
        self.sound_volume = 1
        self.sec1 = 0
        self.sec2 = 0
        self.time_start = 30
        self.time_plus = 1
        self.winb = -1
        self.sec_timer_1 = self.sec_timer_2 = self.time_start
        self.play = False
        self.play_game = False
        self.timer_fall_1 = False
        self.timer_fall_2 = False
        self.pause_game = False
        self.start_timer = False
        self.win_game = 0
        self.running = True
        self.click = True
        self.click_1 = False
        self.click_2 = False
        self.click_3 = False
        self.click_4 = False
        self.click_5 = False
        self.click_6 = False
        self.click_7 = False
        self.click_8 = False
        self.click_9 = False
        self.player_turn = '0'
        self.winner = ' '
        self.win = False
        self.temp_win = True
        self.mark = []
        self.panjang_mark = len(self.mark)
        self.bg_image, self.home_button_image, self.setting_button_image, self.play_button_image, self.rematch_button_image, self.reset_button_image, self.pause_button_image , self.board_game_image, self.board_pause_image, self.help_button_image, self.help_board_image, self.win_board_1_image, self.win_board_2_image, self.x_button_image, self.board_timer_image, self.player_score_image_1, self.player_score_image_2, self.mode_board_image, self.easy_button_image, self.medium_button_image, self.hard_button_image  = set_image_all(self.IMAGE)
        self.line_hr, self.line_vr, self.line_dgl, self.line_dgr=  set_image_all_2(self.IMAGE, self.pilih_object_1, self.pilih_object_2)
        self.bg_tictactoe = pygame.image.load(f"{self.bg_image}")
        self.input_board = [
            ['1','2','3'],
            ['4','5','6'],
            ['7','8','9']
               ]

        self.game_map = [
            ['m',' ',' ','p','h','s','hb',' ',' '],
            [' ',' ','b','b','b',' ',' ','pl','pb'],
            [' ',' ','b','b','b',' ',' ','pa'],
            [' ',' ','b','b','b',' ',' ','st'],
            [' ',' ',' ',' ',' ',' ',' ','rm','x']
            ]

    def createTileMap(self):
        print(f"{self.pilih_object_1, self.pilih_object_2}")
        y = 0
        board = 0
        for row in self.game_map:
            x = 0
            for tile in row:
                if tile == 'hb':
                    self.home_button = GameButton(self, x *TILESIZE +50, y*TILESIZE +10, self.home_button_image)
                if tile == 'b':
                    board += 1
                    self.board = Board(self, x* TILESIZE , y*TILESIZE, self.board_game_image)
                if tile == 'X':
                    self.winner_board_X = Board(self, x*TILESIZE + 70, y*TILESIZE,self.board_game_image)
                if tile == 'O':
                    self.winner_board_O = Board(self, x*TILESIZE - 70, y*TILESIZE,self.board_game_image)
                if tile == 's':
                    self.setting_button = GameButton(self, x *TILESIZE +100, y*TILESIZE +10, self.setting_button_image)
                if tile == 'p':
                    self.play_button = GameButton(self, x *TILESIZE +30 , y*TILESIZE + 30, self.play_button_image)
                if tile == 'rm':
                    self.rematch_button = GameButton(self, x *TILESIZE +30, y*TILESIZE +30, self.rematch_button_image)
                if tile == 'st':
                    self.reset_button = GameButton(self, x *TILESIZE +30, y*TILESIZE +30,self.reset_button_image) 
                if tile == 'pa':
                    self.pause_button = GameButton(self, x *TILESIZE +30 , y*TILESIZE + 30, self.pause_button_image)
                if tile == 'pl':
                    self.playwhilepause_button = GameButton(self, x *TILESIZE +30  , y*TILESIZE  -140, self.play_button_image)
                if tile == 'pb':
                    self.pause_board = ImageBoard(self, x*TILESIZE + 190,  y*TILESIZE + 140, self.board_pause_image, IMAGE_LAYER)
                if tile == 'wb1':
                    self.win_board_1 = ImageBoard(self, x*TILESIZE + 190,  y*TILESIZE + 140, self.win_board_1_image, IMAGE_LAYER)
                if tile == 'wb2':
                    self.win_board_2 = ImageBoard(self, x*TILESIZE + 190,  y*TILESIZE + 140, self.win_board_2_image,IMAGE_LAYER)
                if tile == 'h':
                    self.help_button = GameButton(self, x *TILESIZE +150, y*TILESIZE +10, self.help_button_image)
                if tile == 'x':
                        self.x_button = XButton(self, x *TILESIZE +150, y*TILESIZE +10, self.x_button_image)

                if self.IMAGE == 'NEON':
                    
                    if tile == 'm' and self.play == False:
                        self.mode_board_ = ImageBoard(self, x*TILESIZE + 190,  y*TILESIZE + 140, self.mode_board_image, IMAGE_LAYER)
                        self.easy_board = ImageBoardTictactoe(self, x*TILESIZE + 275,  y*TILESIZE + 290, self.easy_button_image, IMAGE_LAYER + 1)
                        self.medium_board = ImageBoardTictactoe(self, x*TILESIZE + 275,  y*TILESIZE + 350, self.medium_button_image, IMAGE_LAYER + 1)
                        self.hard_board = ImageBoardTictactoe(self, x*TILESIZE + 275,  y*TILESIZE + 420, self.hard_button_image, IMAGE_LAYER + 1)
                        self.easy_button = ModeBoard(self, x*TILESIZE + 280+5,  y*TILESIZE + 290+10, IMAGE_LAYER + 2)
                        self.medium_button = ModeBoard(self, x*TILESIZE + 280+5,  y*TILESIZE + 350+10, IMAGE_LAYER + 2)
                        self.hard_button = ModeBoard(self, x*TILESIZE + 280+5, y*TILESIZE + 420+10, IMAGE_LAYER + 2)
                elif self.IMAGE == 'PIXEL':
                    if tile == 'm' and self.play == False:
                        z = 20
                        q = 15
                        self.mode_board_ = ImageBoard(self, x*TILESIZE + 190,  y*TILESIZE + 140, self.mode_board_image, IMAGE_LAYER)
                        self.easy_board = ImageBoardTictactoe(self, x*TILESIZE + 275-z,  y*TILESIZE + 290+q, self.easy_button_image, IMAGE_LAYER + 1)
                        self.medium_board = ImageBoardTictactoe(self, x*TILESIZE + 275-z,  y*TILESIZE + 350+q, self.medium_button_image, IMAGE_LAYER + 1)
                        self.hard_board = ImageBoardTictactoe(self, x*TILESIZE + 275-z,  y*TILESIZE + 420+q, self.hard_button_image, IMAGE_LAYER + 1)
                        self.easy_button = ModeBoard(self, x*TILESIZE + 280+5-z,  y*TILESIZE + 290+10+q, IMAGE_LAYER + 2)
                        self.medium_button = ModeBoard(self, x*TILESIZE + 280+5-z,  y*TILESIZE + 350+10+q, IMAGE_LAYER + 2)
                        self.hard_button = ModeBoard(self, x*TILESIZE + 280+5-z, y*TILESIZE + 420+10+q, IMAGE_LAYER + 2)
                x += 1
            y += 1

    def createInputBoard(self):
        y = TILESIZE
        for row in self.input_board:
            x = TILESIZE*2
            for tile in row:
                if tile == 'X':
                    self.input_board_X = Player1_Board(self, x, y,self.input_board1_image)
                if tile == 'O':
                    self.input_board_O = Player2_Board(self, x, y,self.input_board2_image)
                if tile == '1':
                    self.input_board_1 = InputBoard(self, x, y)
                if tile == '2':
                    self.input_board_2 = InputBoard(self, x, y)
                if tile == '3':
                    self.input_board_3 = InputBoard(self, x, y)
                if tile == '4':
                    self.input_board_4 = InputBoard(self, x, y)
                if tile == '5':
                    self.input_board_5 = InputBoard(self, x, y)
                if tile == '6':
                    self.input_board_6 = InputBoard(self, x, y)
                if tile == '7':
                    self.input_board_7 = InputBoard(self, x, y)
                if tile == '8':
                    self.input_board_8 = InputBoard(self, x, y)
                if tile == '9':
                    self.input_board_9 = InputBoard(self, x, y)
                x += TILESIZE
            y += TILESIZE

    def pausegame(self):
        self.play_game = False
        self.pause_game = True
        self.start_timer = False
        self.click = False
        self.click_1 = False
        self.click_2 = False
        self.click_3 = False
        self.click_4 = False
        self.click_5 = False
        self.click_6 = False
        self.click_7 = False
        self.click_8 = False
        self.click_9 = False
        # self.game_map[0][0] = 'pa'
        
    def playwhilepause(self):
        self.play_game = True
        self.start_timer = True
        print(f"iniditekan")
        self.pause_game = True
        self.click = True
        self.click_1 = True
        self.click_2 = True
        self.click_3 = True
        self.click_4 = True
        self.click_5 = True
        self.click_6 = True
        self.click_7 = True
        self.click_8 = True
        self.click_9 = True

    def playgame(self):
        if self.play:
            self.easy_button.rect.x = 1000
            self.medium_button.rect.x = 1000
            self.hard_button.rect.x = 1000
            # if self.play_sound:
            #     self.backsound.play()
            #     self.play_sound = False
            if self.play_game == True and self.win_game == 1 and not self.pause_game:
                # self.game_map[4][3] = 'pl'
                self.game_map = [
        ['wb1',' ','',' ','h','s','hb'],
        [' ',' ','b','b','b',' ',' '],
        [' ',' ','b','b','b',' ',' '],
        [' ',' ','b','b','b',' ',' '],
        [' ',' ','st',' ','rm',' ',' ','x']
        ]
            elif self.play_game == True and self.win_game == 2 and not self.pause_game:
                # self.game_map[4][3] = 'pl'
                self.game_map = [
        ['wb2',' ','',' ','h','s','hb'],
        [' ',' ','b','b','b',' ',' '],
        [' ',' ','b','b','b',' ',' '],
        [' ',' ','b','b','b',' ',' '],
        [' ',' ','st',' ','rm',' ',' ','x']
        ]
            elif self.play_game == True:
                # self.game_map[4][3] = 'pa'
                self.klik_diproses = True
                self.playwhilepause_button.rect.x = 1000
                self.game_map = [
        [' ',' ','',' ','h','s','hb'],
        [' ',' ','b','b','b',' ',' '],
        [' ',' ','b','b','b',' ',' '],
        [' ',' ','b','b','b',' ',' '],
        [' ',' ','st','pa','rm',' ',' ','x']
        ]
            elif self.play_game == False and self.pause_game:
                # self.game_map[4][3] = 'pl'
                if self.IMAGE == 'PIXEL':
                    self.playwhilepause_button.rect.y = 390
                    self.playwhilepause_button.rect.x = 450

                self.game_map = [
        ['pb',' ','',' ','h','s','hb'],
        [' ',' ','b','b','b',' ',' '],
        [' ',' ','b','b','b',' ',' '],
        [' ',' ','b','b','b',' ',' '],
        [' ',' ','st','pl','rm',' ',' ','x']
        ]
                
            if self.player_turn == '0':
                self.player_turn = '1'
            if self.win == True:
                self.start_timer = False
                self.game_map = [
        [' ',' ','',' ','h','s','hb'],
        [' ',' ','b','b','b',' ',' '],
        [' ',' ','b','b','b',' ',' '],
        [' ',' ','b','b','b',' ',' '],
        [' ',' ','st',' ','rm',' ',' ','x']
        ]
            if self.win_game == 1:
                
                # self.start_timer = False
                self.game_map = [
        ['wb1',' ','',' ','h','s','hb'],
        [' ',' ','b','b','b',' ',' '],
        [' ',' ','b','b','b',' ',' '],
        [' ',' ','b','b','b',' ',' '],
        [' ',' ','st',' ','rm',' ',' ','x']
        ]
            if self.win_game == 2:
                # self.start_timer = False
                self.game_map = [
        ['wb2',' ','',' ','h','s','hb'],
        [' ',' ','b','b','b',' ',' '],
        [' ',' ','b','b','b',' ',' '],
        [' ',' ','b','b','b',' ',' '],
        [' ',' ','st',' ','rm',' ',' ','x']
        ]
            if self.winb == 0:
                self.line_win_x_0 = ImageBoard(self,280+5,140+45,self.line_hr,6)
            elif self.winb == 1:
                self.line_win_x_1 = ImageBoard(self,280+5,280+45,self.line_hr,6)
            elif self.winb == 2:
                self.line_win_x_2 = ImageBoard(self,280+5,420+45,self.line_hr,6)
            if self.winb == 10:
                self.line_win_y_0 = ImageBoard(self,280+42.5,140+5,self.line_vr,6)  
            elif self.winb == 11: 
                self.line_win_y_1 = ImageBoard(self,420+42.5,140+5,self.line_vr,6) 
            elif self.winb == 12: 
                self.line_win_y_2 = ImageBoard(self,560+42.5,140+5,self.line_vr,6) 
            if self.winb == 20:
                self.line_win_dg_1 = ImageBoard(self,280,140,self.line_dgl,6)
            elif self.winb == 30:
                self.line_win_dg_2 = ImageBoard(self,280,140-3,self.line_dgr,6)
            
            if self.IMAGE == 'NEON':
                self.board_timer = ImageBoard(self, 280,-15, self.board_timer_image, 4)
                self.display_timer1 = TimerText(self,370,62,self.sec_timer_1, self.warna)
                self.display_timer1.update_text(self.sec_timer_1, self.warna)
                self.display_timer2 = TimerText(self,547,62,self.sec_timer_2, self.warna)
                self.display_timer2.update_text(self.sec_timer_2, self.warna)
            elif self.IMAGE == 'PIXEL':
                
                self.board_timer = ImageBoard(self, 280+20,-15-6,self.board_timer_image, 4)
                self.display_timer1 = TimerText(self,370,40,self.sec_timer_1, self.warna)
                self.display_timer1.update_text(self.sec_timer_1, self.warna)
                self.display_timer2 = TimerText(self,547,40,self.sec_timer_2, self.warna)
                self.display_timer2.update_text(self.sec_timer_2, self.warna)
            self.board_score_1 = ImageBoard(self, 0, 175, self.player_score_image_1, 4)
            self.board_score_2 = ImageBoard(self, 700, 175, self.player_score_image_2, 4)
            self.board_s1 = Board(self, 70 , 280, self.board_game_image)
            self.board_s2 = Board(self, 770, 280, self.board_game_image)
            self.display_score_1 = ScoreText(self, 115, 305, f'{self.score_count_1}', self.warna)
            self.display_score_2 = ScoreText(self, 815, 305, f'{self.score_count_2}', self.warna)
            
            
            # self.mid_timer = TimerTextmid(self,490,57,':')
        
    def resetboard(self):
        self.winner = ' '
        self.win_game = 0
        self.winb = -1
        self.play_game = True
        self.player_turn = '1'
        self.temp_win = True
        self.click = False
        self.click_1 = True
        self.click_2 = True
        self.click_3 = True
        self.click_4 = True
        self.click_5 = True
        self.click_6 = True
        self.click_7 = True
        self.click_8 = True
        self.click_9 = True
        self.win = False
        self.start_timer = False
        self.sec_timer_1 = self.sec_timer_2 =  self.time_start
         

        self.mark = []
        self.panjang_mark = len(self.mark)
        self.input_board = [
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9']
        ]   
        self.game_map = [
        [' ',' ','',' ','h','s','hb'],
        [' ',' ','b','b','b',' ',' '],
        [' ',' ','b','b','b',' ',' '],
        [' ',' ','b','b','b',' ',' '],
        [' ',' ','st',' ','rm',' ',' ','x']
        ]

    def resetgame(self):
        self.play = False
        self.win_game = 0
        self.time_start = 30
        self.play_game = False
        self.winner = ' '
        self.winb = -1
        self.player_turn = '1'
        self.temp_win = True
        self.click = False
        self.click_1 = False
        self.click_2 = False
        self.click_3 = False
        self.click_4 = False
        self.click_5 = False
        self.click_6 = False
        self.click_7 = False
        self.click_8 = False
        self.click_9 = False
        self.win = False
        self.mark = []
        self.panjang_mark = len(self.mark)
        self.score_count_1 = 0
        self.score_count_2 = 0
        self.sec_timer_1 = self.sec_timer_2 = self.time_start
        self.play = False
        self.start_timer = False
        self.input_board = [
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9']
        ]  

        self.game_map = [
        ['m',' ',' ','p','h','s','hb'],
        [' ',' ','b','b','b',' ',' '],
        [' ',' ','b','b','b',' ',' '],
        [' ',' ','b','b','b',' ',' '],
        [' ',' ',' ',' ',' ',' ','x']
        ]

    def cek_click(self):
        mx, my = pygame.mouse.get_pos()
        self.klik_diproses = False
        if self.click_button_game:
            if self.home_button.rect.collidepoint((mx, my)):
                if self.click:
                    # self.backsound.stop()
                    CLICKSOUND.play()
                    GAMESOUND.stop()
                    self.home_button.set_alpha(255)
                    print(f"{self.home_button.rect.x}")
                    self.running = False
                    self.home_button.alpha = 255

            if self.play_button.rect.collidepoint((mx, my)):
                if self.click:
                    CLICKSOUND.play()
                    self.play_button.set_alpha(255)
                    # self.play_sound = True
                    self.play_button.alpha = 255
                    self.play = True
                    self.play_game = True
                    self.start_timer = False
                    self.play_button.alpha = 255
                    self.help = False
                    # self.rematch_button.rect.x = 450
                    # self.rematch_button.rect.y = 590
                    self.click = False
                    self.click_1 = True
                    self.click_2 = True
                    self.click_3 = True
                    self.click_4 = True
                    self.click_5 = True
                    self.click_6 = True
                    self.click_7 = True
                    self.click_8 = True
                    self.click_9 = True
                    self.player_turn = '1'
                    self.game_map = [
                [' ',' ',' ',' ','h','s','hb'],
                [' ',' ','b','b','b',' ',' '],
                [' ',' ','b','b','b',' ',' '],
                [' ',' ','b','b','b',' ',' ',],
                [' ',' ','st',' ','rm',' ','x']
                ]
                    
            if self.easy_button.rect.collidepoint((mx, my)):
                if self.click and self.clik_mode:
                    CLICKSOUND.play()
                    # self.play_sound = True
                    self.play = True
                    self.play_game = True
                    self.start_timer = False
                    self.time_plus = 2
                    self.time_start = 25
                    self.play_button.alpha = 255
                    self.help = False
                    # self.rematch_button.rect.x = 450
                    # self.rematch_button.rect.y = 590
                    self.click = False
                    self.click_1 = True
                    self.click_2 = True
                    self.click_3 = True
                    self.click_4 = True
                    self.click_5 = True
                    self.click_6 = True
                    self.click_7 = True
                    self.click_8 = True
                    self.click_9 = True
                    self.player_turn = '1'
                    self.game_map = [
                [' ',' ',' ',' ','h','s','hb'],
                [' ',' ','b','b','b',' ',' '],
                [' ',' ','b','b','b',' ',' '],
                [' ',' ','b','b','b',' ',' ',],
                [' ',' ','st',' ','rm',' ','x']
                ]
                    
            if self.medium_button.rect.collidepoint((mx, my)):
                if self.click and self.clik_mode:
                    CLICKSOUND.play()
                    # self.play_sound = True
                    self.play = True
                    self.play_game = True
                    self.start_timer = False
                    self.time_plus = 1
                    self.time_start = 15
                    self.play_button.alpha = 255
                    self.help = False
                    # self.rematch_button.rect.x = 450
                    # self.rematch_button.rect.y = 590
                    self.click = False
                    self.click_1 = True
                    self.click_2 = True
                    self.click_3 = True
                    self.click_4 = True
                    self.click_5 = True
                    self.click_6 = True
                    self.click_7 = True
                    self.click_8 = True
                    self.click_9 = True
                    self.player_turn = '1'
                    self.game_map = [
                [' ',' ',' ',' ','h','s','hb'],
                [' ',' ','b','b','b',' ',' '],
                [' ',' ','b','b','b',' ',' '],
                [' ',' ','b','b','b',' ',' ',],
                [' ',' ','st',' ','rm',' ','x']
                ]
                    
            if self.hard_button.rect.collidepoint((mx, my)):
                if self.click and self.clik_mode:
                    CLICKSOUND.play()
                    # self.play_sound = True
                    self.play = True
                    self.play_game = True
                    self.start_timer = False
                    self.time_plus = 1
                    self.time_start = 5
                    self.play_button.alpha = 255
                    self.help = False
                    # self.rematch_button.rect.x = 450
                    # self.rematch_button.rect.y = 590
                    self.click = False
                    self.click_1 = True
                    self.click_2 = True
                    self.click_3 = True
                    self.click_4 = True
                    self.click_5 = True
                    self.click_6 = True
                    self.click_7 = True
                    self.click_8 = True
                    self.click_9 = True
                    self.player_turn = '1'
                    self.game_map = [
                [' ',' ',' ',' ','h','s','hb'],
                [' ',' ','b','b','b',' ',' '],
                [' ',' ','b','b','b',' ',' '],
                [' ',' ','b','b','b',' ',' ',],
                [' ',' ','st',' ','rm',' ','x']
                ]

            if self.rematch_button.rect.collidepoint((mx, my)):
                if self.click:
                    CLICKSOUND.play()
                    self.rematch_button.set_alpha(255)
                    self.resetboard()

            if self.help_button.rect.collidepoint((mx, my)):
                if self.click:
                    self.click = False
                    self.start_timer = False
                    self.click_button_game = False
                    self.help_button.set_alpha(255)
                    CLICKSOUND.play()
                    self.help = True

            
                    # self.x_button.rect.x = 1000
                    # self.x_button.rect.y = 1000

                # self.x_button.set_layer(12)
            if self.pause_button.rect.collidepoint((mx, my)):
                if self.click:
                    self.pausegame()
                    set_global_volume(0)
                    self.pause_button.alpha = 255
                    CLICKSOUND.play()
                    print(f"ditekanpause")
                    print(f"{self.play_game}")

            if self.setting_button.rect.collidepoint((mx, my)):
                if self.click:
                    self.setting_button.set_alpha(255)
                    if self.sound_volume > 0:
                        self.sound_volume -= 0.1
                    set_global_volume(self.sound_volume)
                    CLICKSOUND.play()
                    # print(f"ditekanpause")
                    # print(f"{self.play_game}")

            if self.playwhilepause_button.rect.collidepoint((mx, my)) and not self.klik_diproses:
                if self.click:
                    print(f"iniditekanplay")
                    self.playwhilepause()
                    toggle_music_pause()
                    CLICKSOUND.play()
                    set_global_volume(self.sound_volume)
                    self.playwhilepause_button.set_alpha(255)
                    print(f"{self.play_game}")
                    self.klik_diproses = True

            if self.reset_button.rect.collidepoint((mx, my)):
                if self.click:
                    self.reset_button.alpha = 255
                    self.resetgame()
                    CLICKSOUND.play()
                    self.reset_button.set_alpha(255)

            if self.input_board_1.rect.collidepoint((mx,my)) and self.click_1:
                if self.click:
                    if self.player_turn == '1':
                        self.input_board[0][0] = 'X'
                        self.player_turn = '2'
                        self.sec_timer_1 += self.time_plus
                        self.mark.append([0,0])
                        print(f"{self.player_turn}")
                    else :
                        self.input_board[0][0] = 'O'
                        self.player_turn = '1'
                        self.sec_timer_2 += self.time_plus
                        self.mark.append([0,0])
                        print(f"{self.player_turn}")
                    self.start_timer = True
                    self.click_1 = False

            if self.input_board_2.rect.collidepoint((mx,my)) and self.click_2:
                if self.click:
                    if self.player_turn == '1':
                        self.input_board[0][1] = 'X'
                        self.player_turn = '2'
                        self.sec_timer_1 += self.time_plus
                        self.mark.append([0,1])
                        print(f"{self.player_turn}")
                    else :
                        self.input_board[0][1] = 'O'
                        self.player_turn = '1'
                        self.sec_timer_2 += self.time_plus
                        self.mark.append([0,1])
                        print(f"{self.player_turn}")
                    self.start_timer = True
                    self.click_2 = False

            if self.input_board_3.rect.collidepoint((mx,my)) and self.click_3:
                if self.click:
                    if self.player_turn == '1':
                        self.input_board[0][2] = 'X'
                        self.player_turn = '2'
                        self.sec_timer_1 += self.time_plus
                        self.mark.append([0,2])
                        print(f"{self.player_turn}")
                    else :
                        self.input_board[0][2] = 'O'
                        self.player_turn = '1'
                        self.sec_timer_2 += self.time_plus
                        self.mark.append([0,2])
                        print(f"{self.player_turn}")
                    self.start_timer = True
                    self.click_3 = False

            if self.input_board_4.rect.collidepoint((mx,my)) and self.click_4:
                if self.click:
                    if self.player_turn == '1':
                        self.input_board[1][0] = 'X'
                        self.player_turn = '2'
                        self.sec_timer_1 += self.time_plus
                        self.mark.append([1,0])
                        print(f"{self.player_turn}")
                    else :
                        self.input_board[1][0] = 'O'
                        self.player_turn = '1'
                        self.sec_timer_2 += self.time_plus
                        self.mark.append([1,0])
                        print(f"{self.player_turn}")
                    self.start_timer = True
                    self.click_4 = False

            if self.input_board_5.rect.collidepoint((mx,my)) and self.click_5:
                if self.click:
                    if self.player_turn == '1':
                        self.input_board[1][1] = 'X'
                        self.player_turn = '2'
                        self.sec_timer_1 += self.time_plus
                        self.mark.append([1,1])
                        print(f"{self.player_turn}")
                    else :
                        self.input_board[1][1] = 'O'
                        self.player_turn = '1'
                        self.sec_timer_2 += self.time_plus
                        self.mark.append([1,1])
                        print(f"{self.player_turn}")
                    self.start_timer = True
                    self.click_5 = False

            if self.input_board_6.rect.collidepoint((mx,my)) and self.click_6:
                if self.click:
                    if self.player_turn == '1':
                        self.input_board[1][2] = 'X'
                        self.player_turn = '2'
                        self.sec_timer_1 += self.time_plus
                        self.mark.append([1,2])
                        print(f"{self.player_turn}")
                    else :
                        self.input_board[1][2] = 'O'
                        self.player_turn = '1'
                        self.sec_timer_2 += self.time_plus
                        self.mark.append([1,2])
                        print(f"{self.player_turn}")
                    self.start_timer = True
                    self.click_6 = False

            if self.input_board_7.rect.collidepoint((mx,my)) and self.click_7:
                if self.click:
                    if self.player_turn == '1':
                        self.input_board[2][0] = 'X'
                        self.player_turn = '2'
                        self.sec_timer_1 += self.time_plus
                        self.mark.append([2,0])
                        print(f"{self.player_turn}")
                    else :

                        self.input_board[2][0] = 'O'
                        self.player_turn = '1'
                        self.sec_timer_2 += self.time_plus
                        self.mark.append([2,0])
                        print(f"{self.player_turn}")
                    self.start_timer = True
                    self.click_7 = False

            if self.input_board_8.rect.collidepoint((mx,my)) and self.click_8 and not self.klik_diproses:
                if self.click:
                    if self.player_turn == '1':
                        self.input_board[2][1] = 'X'
                        self.player_turn = '2'
                        self.sec_timer_1 += self.time_plus
                        self.mark.append([2,1])
                        print(f"{self.player_turn}")
                    else :
                        self.input_board[2][1] = 'O'
                        self.player_turn = '1'
                        self.sec_timer_2 += self.time_plus
                        self.mark.append([2,1])
                        print(f"{self.player_turn}")
                    self.start_timer = True
                    self.click_8 = False

            if self.input_board_9.rect.collidepoint((mx,my)) and self.click_9:
                if self.click:
                    if self.player_turn == '1':
                        self.input_board[2][2] = 'X'
                        self.player_turn = '2'
                        self.sec_timer_1 += self.time_plus
                        self.mark.append([2,2])
                        print(f"{self.player_turn}")
                    else :
                        self.input_board[2][2] = 'O'
                        self.player_turn = '1'
                        self.sec_timer_2 += self.time_plus
                        self.mark.append([2,2])
                        print(f"{self.player_turn}")
                    self.start_timer = True
                    self.click_9 = False
        if self.x_button.rect.collidepoint((mx, my)):
            if self.click:
                self.help_button.set_alpha(255)
                CLICKSOUND.play()
                self.help = False
                if self.play_game == True:
                    self.start_timer = True
                self.click_button_game = True
        self.cek_langkah_6()

    def sort(self, mark):
        for i in range(1, len(mark)):

            mark[i-1] = mark[i]
        mark.pop() 
        return mark
    
    def timerdesc(self):
        if self.player_turn == '1':
            self.sec_timer_1 -= 1
            TIMERSOUND.play()
        elif self.player_turn == '2':
            self.sec_timer_2 -= 1
            TIMERSOUND.play()

    def cek_langkah_6(self):
        if len(self.mark) == 6 :
            if self.mark[0] == [0,0]:
                self.input_board[0][0] = '1'
                self.click_1 = True
            elif self.mark[0] == [0,1]:
                self.input_board[0][1] = '2'
                self.click_2 = True
            elif self.mark[0] == [0,2]:
                self.input_board[0][2] = '3' 
                self.click_3 = True
            elif self.mark[0] == [1,0]:
                self.input_board[1][0] = '4'
                self.click_4 = True 
            elif self.mark[0] == [1,1]:
                self.input_board[1][1] = '5' 
                self.click_5 = True
            elif self.mark[0] == [1,2]:
                self.input_board[1][2] = '6' 
                self.click_6 = True
            elif self.mark[0] == [2,0]:
                self.input_board[2][0] = '7' 
                self.click_7 = True
            elif self.mark[0] == [2,1]:
                self.input_board[2][1] = '8'
                self.click_8 = True 
            elif self.mark[0] == [2,2]:
                self.input_board[2][2] = '9'
                self.click_9 = True
            self.sort(self.mark)

    def cek_winner(self,arr):
        panjang_arr = len(arr)
        cekX = 'X'
        cekO = 'O'

        for i in range(panjang_arr):
            for j in range(panjang_arr):
                if arr[i][j] == cekX:
                    if j == panjang_arr-1:
                        self.temp_win = False
                        self.winner = '1'
                        print(i)
                        if i == 0:
                            self.winb = 0
                        elif i == 1:
                            self.winb = 1
                        elif i == 2:
                            self.winb = 2
                        print(f"{i},{j}")
                        print("Player 1 Menang")
                else :
                    break
    #o
        for i in range(panjang_arr):
            for j in range(panjang_arr):
                if arr[i][j] == cekO:
                    if j == panjang_arr-1:
                        self.temp_win = False
                        self.winner = '2'
                        if i == 0:
                            self.winb = 0
                        elif i == 1:
                            self.winb = 1
                        elif i == 2:
                            self.winb = 2
                        print(f"{i},{j}")
                        print("Player 2 Menang")
                else :
                    break
    #vertikal
    #X
        for i in range(0,panjang_arr):
            for j in range(0,panjang_arr):
                if arr[j][i] == cekX :
                    # cek == arr[j][i]
                    if j == panjang_arr-1:
                        if i == 0:
                            self.winb = 10
                        elif i == 1:
                            self.winb = 11
                        elif i == 2:
                            self.winb = 12
                        self.temp_win = False
                        print(f"{j},{i}")
                        self.winner = '1'
                        print("Player 1 Menang")
                else :
                    break
    #O
        for i in range(0,panjang_arr):
            for j in range(0,panjang_arr):
                if arr[j][i] == cekO:
                    # cek == arr[j][i]
                    if j == panjang_arr-1:
                        self.temp_win = False
                        self.winner = '2'
                        if i == 0:
                            self.winb = 10
                        elif i == 1:
                            self.winb = 11
                        elif i == 2:
                            self.winb = 12
                        print(f"{j},{i}")
                        print("Player 2 Menang")
                else :
                    break
        
    #diagonal
    #X        
        if arr[0][0] == 'X' and arr[1][1] == 'X' and arr[2][2] == 'X' or arr[0][2] == 'X' and arr[1][1] == 'X' and arr[2][0] == 'X':
            self.temp_win = False
            self.winner = '1'
            if arr[0][0] == 'X' and arr[1][1] == 'X' and arr[2][2] == 'X':
                self.winb = 20
            elif arr[0][2] == 'X' and arr[1][1] == 'X' and arr[2][0] == 'X':
                self.winb = 30
            print("Player 1 Menang")
    #O
        if arr[0][0] == 'O' and arr[1][1] == 'O' and arr[2][2] == 'O' or arr[0][2] == 'O' and arr[1][1] == 'O' and arr[2][0] == 'O':
            self.temp_win = False
            self.winner = '2'
            self.winb = 30     
            if arr[0][0] == 'O' and arr[1][1] == 'O' and arr[2][2] == 'O':
                self.winb = 20
            elif arr[0][2] == 'O' and arr[1][1] == 'O' and arr[2][0] == 'O':
                self.winb = 30
            print("Player 2 Menang")

        if self.winner == '1' or self.winner == '2':
            self.start_timer = False
            print(self.game_map[2][0])
            print(self.game_map[2][6])
            self.click_1 = False
            self.click_2 = False
            self.click_3 = False
            self.click_4 = False
            self.click_5 = False
            self.click_6 = False
            self.click_7 = False
            self.click_8 = False
            self.click_9 = False
        
        if self.winner == '1':
            # self.game_map[2][0] = 'X'
            # self.start_timer = False
            # self.play_game = False
            self.pause_game = False
            self.win = True
            self.win_game = 1
            WINSOUND.play()
            self.winner = '0'
            self.score_count_1 = self.score_count_1 + 1
            self.display_score_1.update_text(self.score_count_1, self.warna)
        elif self.winner == '2':
            # self.game_map[2][6] = 'O'
            self.pause_game = False
            self.win = True
            self.win_game = 2
            WINSOUND.play()
            self.winner = '0'
            # self.start_timer = False
            self.score_count_2 = self.score_count_2 + 1
            self.display_score_2.update_text(self.score_count_2, self.warna)
        
        if self.sec_timer_1 == 0 and self.win == False:
            # self.sec_timer_1 -= -1
            self.winner = '2'
        elif self.sec_timer_2 == 0 and self.win == False:
            # self.sec_timer_2 -= -1
            self.winner = '1'

    def new(self):
        self.all_sprites_tictactoe = pygame.sprite.LayeredUpdates()
        self.createTileMap()
        self.createInputBoard()
    
    def keyboard_input(self,event):
        if event.key == pygame.K_1 and self.click_1:
            self.start_timer = True
            print("apa")
            if self.player_turn == '1':
                self.input_board[0][0] = 'X'
                self.sec_timer_1 += self.time_plus
                self.player_turn = '2'
                self.mark.append([0,0])
                print(f"{self.player_turn}")
            else :
                self.input_board[0][0] = 'O'
                self.player_turn = '1'
                self.mark.append([0,0])
                self.sec_timer_2 += self.time_plus
                print(f"{self.player_turn}")
            self.click_1 = False
        if event.key == pygame.K_2 and self.click_2:
            self.start_timer = True
            print("apa")
            if self.player_turn == '1':
                self.input_board[0][1] = 'X'
                self.sec_timer_1 += self.time_plus
                self.player_turn = '2'
                self.mark.append([0,1])
                print(f"{self.player_turn}")
            else :
                self.input_board[0][1] = 'O'
                self.player_turn = '1'
                self.sec_timer_2 += self.time_plus
                self.mark.append([0,1])
                print(f"{self.player_turn}")
            self.click_2 = False
        if event.key == pygame.K_3 and self.click_3:
            self.start_timer = True
            print("apa")
            if self.player_turn == '1':
                self.input_board[0][2] = 'X'
                self.player_turn = '2'
                self.sec_timer_1 += self.time_plus
                self.mark.append([0,2])
                print(f"{self.player_turn}")
            else :
                self.input_board[0][2] = 'O'
                self.player_turn = '1'
                self.sec_timer_2 += self.time_plus
                self.mark.append([0,2])
                print(f"{self.player_turn}")
            self.click_3 = False
        if event.key == pygame.K_4 and self.click_4:
            self.start_timer = True
            print("apa")
            if self.player_turn == '1':
                self.input_board[1][0] = 'X'
                self.player_turn = '2'
                self.sec_timer_1 += self.time_plus
                self.mark.append([1,0])
                print(f"{self.player_turn}")
            else :
                self.input_board[1][0] = 'O'
                self.player_turn = '1'
                self.sec_timer_2 += self.time_plus
                self.mark.append([1,0])
                print(f"{self.player_turn}")
            self.click_4 = False
        if event.key == pygame.K_5 and self.click_5:
            self.start_timer = True
            print("apa")
            if self.player_turn == '1':
                self.input_board[1][1] = 'X'
                self.player_turn = '2'
                self.sec_timer_1 += self.time_plus
                self.mark.append([1,1])
                print(f"{self.player_turn}")
            else :
                self.input_board[1][1] = 'O'
                self.player_turn = '1'
                self.sec_timer_2 += self.time_plus
                self.mark.append([1,1])
                print(f"{self.player_turn}")
            self.click_5 = False
        if event.key == pygame.K_6 and self.click_6:
            self.start_timer = True
            print("apa")
            if self.player_turn == '1':
                self.input_board[1][2] = 'X'
                self.player_turn = '2'
                self.sec_timer_1 += self.time_plus
                self.mark.append([1,2])
                print(f"{self.player_turn}")
            else :
                self.input_board[1][2] = 'O'
                self.player_turn = '1'
                self.sec_timer_2 += self.time_plus
                self.mark.append([1,2])
                print(f"{self.player_turn}")
            self.click_6 = False
        if event.key == pygame.K_7 and self.click_7:
            self.start_timer = True
            print("apa")
            if self.player_turn == '1':
                self.input_board[2][0] = 'X'
                self.player_turn = '2'
                self.sec_timer_1 += self.time_plus
                self.mark.append([2,0])
                print(f"{self.player_turn}")
            else :
                self.input_board[2][0] = 'O'
                self.player_turn = '1'
                self.sec_timer_2 += self.time_plus
                self.mark.append([2,0])
                print(f"{self.player_turn}")
            self.click_7 = False
        if event.key == pygame.K_8 and self.click_8:
            self.start_timer = True
            print("apa")
            if self.player_turn == '1':
                self.input_board[2][1] = 'X'
                self.sec_timer_1 += self.time_plus
                self.player_turn = '2'
                self.mark.append([2,1])
                print(f"{self.player_turn}")
            else :
                self.input_board[2][1] = 'O'
                self.player_turn = '1'
                self.sec_timer_2 += self.time_plus
                self.mark.append([2,1])
                print(f"{self.player_turn}")
            self.click_8 = False
        if event.key == pygame.K_9 and self.click_9:
            self.start_timer = True
            print("apa")
            if self.player_turn == '1':
                self.input_board[2][2] = 'X'
                self.sec_timer_1 += self.time_plus
                self.player_turn = '2'
                self.mark.append([2,2])
                print(f"{self.player_turn}")
            else :
                self.input_board[2][2] = 'O'
                self.player_turn = '1'
                self.sec_timer_2 += self.time_plus
                self.mark.append([2,2])
                print(f"{self.player_turn}")
            self.click_9 = False
        
    def event(self):
        if self.mode_start_time == 0:
            self.clik_mode = True
        if self.IMAGE == 'NEON':
            if self.pilih_object_1 == '1':
                self.input_board1_image = "asset/board/CsB.png" 
            elif self.pilih_object_1 == '2':
                self.input_board1_image = "asset/board/TrB.png"
            else:
                self.input_board1_image = "asset/board/CsB.png"

            if self.pilih_object_2 == '1':
                self.input_board2_image = "asset/board/CrB.png"
            elif self.pilih_object_2 == '2':
                self.input_board2_image = "asset/board/SqB.png"
            else:
               self.input_board2_image = "asset/board/CrB.png"
        elif self.IMAGE == 'PIXEL':
            if self.pilih_object_1 == '1':
                self.input_board1_image = "asset/object/Silang_Pixel.png" 
            elif self.pilih_object_1 == '2':
                self.input_board1_image = "asset/object/Segitiga_Pixel.png"
            else:
                self.input_board1_image = "asset/object/Silang_Pixel.png"

            if self.pilih_object_2 == '1':
                self.input_board2_image = "asset/object/Lingkaran_Pixel.png"
            elif self.pilih_object_2 == '2':
                self.input_board2_image = "asset/object/Kotak_Pixel.png"
            else:
               self.input_board2_image = "asset/object/Lingkaran_Pixel.png"
        if self.help == True:
            if self.IMAGE == 'NEON':
                self.x_button.rect.x = 730
                self.x_button.rect.y = 125
            elif self.IMAGE == 'PIXEL':
                self.x_button.rect.x = 695
                self.x_button.rect.y = 182.5
            # self.x_button = XButton(self, 730, 125, self.x_button_image)
            if self.IMAGE == 'NEON':
                self.help_board = HelpBoard(self, 68, 61, self.help_board_image)
            elif self.IMAGE == 'PIXEL':
                self.help_board = HelpBoard(self, 140, 116, self.help_board_image)
        # elif self.help == False:
            # self.x_button.rect.x = 1000
            # self.x_button.rect.y = 1000

        if self.IMAGE == 'NEON':
            self.warna= WHITE
        elif self.IMAGE == 'PIXEL':
            self.warna = BROWN
        self.cek_click()
        
        if self.temp_win == True:
            self.cek_winner(self.input_board)
            self.tem_win = False
            # print(f"{self.winner}")
        self.click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True
            if event.type == pygame.KEYDOWN:
                self.keyboard_input(event)
            if event.type == pygame.USEREVENT:
                if self.mode_start_time > 0:
                    self.mode_start_time -= 1

            if event.type == pygame.USEREVENT and self.start_timer:
                self.timerdesc()
        if self.sec_timer_1 > self.time_start:  
            self.sec_timer_1 = self.time_start
        if self.sec_timer_2 > self.time_start:
            self.sec_timer_2 = self.time_start
            # self.setting_button.cek_click(event)

    def draw(self):
        
        self.playgame()
        
        self.screen.blit(self.bg_tictactoe, (0,0))
        self.all_sprites_tictactoe.draw(self.screen)
        # self.all_sprites_tictactoe.empty()
        pygame.display.update()
        
    def update(self):
        self.all_sprites_tictactoe.update()
        
    def main(self):
        GAMESOUND.play(loops=-1)
        # GAMESOUND.set_volume(0.5)
        while self.running:
            self.new()
            self.event()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        self.running = False
        return self.bg_image

# tt = Tictactoe(bg_game, '1', '1')
# tt.main()


        