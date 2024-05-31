import pygame
from abc import ABC, abstractmethod

pygame.mixer.init()
S_WIDTH = 980
S_HEIGHT = 700

TILESIZE = 140

FPS = 60

RED = (255,0,0)
BLACK = (0,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)
BROWN = (91,51,60)

LAYER = 1
BOARD_LAYER = 1
REMATCH_LAYER = 0
INPUT_BOARD_LAYER = 2
INPUT_BOARD_X_LAYER = 3
INPUT_BOARD_Y_LAYER = 3
GAMEBUTTONLAYER = 11
IMAGE_LAYER = 9

# board 1[2][1], x = 280 , y = 140
# board 2[3][1], x = 420 , y = 140
# board 3[4][1], x = 560 , y = 140
# board 4[2][2], x = 280 , y = 280
# board 5[3][2], x = 420 , y = 280
# board 6[4][2], x = 560 , y = 280
# board 7[2][3], x = 280 , y = 420
# board 8[3][3], x = 420 , y = 420
# board 9[4][3], x = 560 , y = 420

# input_board = [
#             ['1','2','3'],
#             ['4','5','6'],
#             ['7','8','9']
#                ]

class MENU(ABC):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.click = False

    @abstractmethod
    def new(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def main(self):
        pass

    @abstractmethod
    def event(self):
        pass

GAMESOUND = pygame.mixer.Sound('asset/sound/1148818_Cyberpunk (1).wav')
WINSOUND = pygame.mixer.Sound('asset/sound/mixkit-video-game-win-2016.wav')
TIMERSOUND = pygame.mixer.Sound('asset/sound/mixkit-click-melodic-tone-1129.wav')
CLICKSOUND = pygame.mixer.Sound('asset/sound/mixkit-game-click-1114.wav')

def set_global_volume(volume):
    # Set volume for music
    pygame.mixer.music.set_volume(volume)
    
    # Set volume for all sound channels
    for i in range(pygame.mixer.get_num_channels()):
        pygame.mixer.Channel(i).set_volume(volume)

def toggle_music_pause():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

#player 1 win = game_map[2][2] = ' '
#player 2 win = game_map[2][6] = ' '
game_map = [
            [' ',' ',' ',' ',' ',' ','hb'],
            [' ',' ','b','b','b',' ',' '],
            [' ',' ','b','b','b',' ',' '],
            [' ',' ','b','b','b',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ']
            ]


bg_intro = "asset/background/Intro.png"
bg_theme = "asset/background/Intro.png"
bg_game = "asset/background/game_bg.png"
bg_credit = "asset/background/Credits.png"

def set_image_all(image):
     
    global bg_game, home_button, setting_button, play_button, rematch_button, reset_button, pause_button, board_game, board_pause, help_button, help_board, win_board1, win_board2, x_buttton, timer_board, player1, player2, mode_board, easy_button, medium_button, hard_button
    if image == 'NEON':
         
        bg_game = "asset/background/game_bg.png"
        home_button = "asset/button/BN_Home.png"
        setting_button = "asset/button/BN_Settings.png"
        play_button = "asset/button/BN_Play.png"
        rematch_button = "asset/button/BN_retry.png"
        reset_button = "asset/button/BN_reset.png"
        pause_button = "asset/button/BN_Pause.png"
        board_game = "asset/board/Board_neon.png"
        board_pause = "asset/board/Neon_Paused.png"
        help_button = "asset/button/BN_help.png"
        help_board = "asset/board/HELP_NEON.png"
        win_board1 = "asset/board/Neon_P1W.png"
        win_board2 = "asset/board/Neon_P2W.png"
        x_button = "asset/button/exit neon.png"
        timer_board = "asset/board/Neon_Timer.png"
        player1 = "asset/player/P1.png"
        player2 = "asset/player/P2.png"
        mode_board = "asset/board/Difficulty_Neon.png"
        easy_button = "asset/button/DF_Easy_Ne.png"
        hard_button = "asset/button/DF_Hard_Ne.png"
        medium_button = "asset/button/DF_Medium_Ne.png"


    if image == 'PIXEL':
        bg_game = "asset/background/Pixel_Game2.png"
        home_button = "asset/button/BP_home.png"
        setting_button = "asset/button/BP_setting.png"
        rematch_button = "asset/button/BP_rematch.png"
        reset_button = "asset/button/BP_reset.png"
        play_button = "asset/button/BP_Play.png"
        pause_button = "asset/button/BP_pause.png"
        board_game = "asset/board/Pixel_Board.png"
        board_pause = "asset/board/Pixel_Paused.png"
        help_button = "asset/button/BP_help.png"
        help_board = "asset/board/HELP_PX.png"
        win_board1 = "asset/board/Pixel_P1W.png"
        win_board2 = "asset/board/Pixel_P2W.png"
        x_button = "asset/button/exit px.png"
        timer_board = "asset/board/Pixel_Timer.png"
        player1 = "asset/player/Pixel_P1.png"
        player2 = "asset/player/Pixel_P2.png"
        mode_board = "asset/board/Difficulty_Pixel.png"
        easy_button = "asset/button/DF_Easy_Px.png"
        hard_button = "asset/button/DF_Hard_Px.png"
        medium_button = "asset/button/DF_Medium_Px.png"
                
    return bg_game, home_button, setting_button, play_button, rematch_button, reset_button, pause_button, board_game, board_pause, help_button, help_board, win_board1, win_board2, x_button, timer_board, player1, player2, mode_board, easy_button, medium_button, hard_button


def set_image_all_2(image, o1,o2):
    global line_hr, line_vr, line_dgl, line_dgr, object_player1, object_player2
    if image == 'NEON':
        if o1 == 1:
            object_player1 = "asset/board/CsB.png"
        elif o1 == 2:
            object_player1 = "asset/board/TrB.png"
        else:
            object_player1 = "asset/board/CsB.png"

        if o2 == 1:
            object_player2 = "asset/board/CrB.png"
        elif o2 == 2:
            object_player2 = "asset/board/SqB.png"
        else:
            object_player2 = "asset/board/CrB.png" 
        line_hr = "asset/board/line_neon_hr.png"
        line_vr = "asset/board/line_neon_vr.png"
        line_dgl = "asset/board/line_neon_dg_l.png"
        line_dgr = "asset/board/line_neon_dg_r.png"

    if image == 'PIXEL':
        if o1 == '1':
            object_player1 = "asset/button/Object_Cs_Px.png"
        elif o1 == '2':
            object_player1 = "asset/button/Object_Tr_Px.png"
        else:
            object_player1 = "asset/board/CsB.png"

        if o2 == '1':
            object_player2 = "asset/button/Object_Cr_Px.png"
        elif o2 == '2':
            object_player2 = "asset/button/Object_Sq_Px.png"
        else:
            object_player2 = "asset/button/Object_Cr_Px.png"
        line_hr = "asset/board/line_neon_hr.png"
        line_vr = "asset/board/line_neon_vr.png"
        line_dgl = "asset/board/line_neon_dg_l.png"
        line_dgr = "asset/board/line_neon_dg_r.png"

    return line_hr, line_vr, line_dgl, line_dgr

