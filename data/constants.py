__author__ = 'justinarmstrong'

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)

ORIGINAL_CAPTION = "Super Mario Bros - Nivel 1"

## COLORS ##

#            R    G    B
GRAY         = (100, 100, 100)
NAVYBLUE     = ( 60,  60, 100)
WHITE        = (255, 255, 255)
RED          = (255,   0,   0)
GREEN        = (  0, 255,   0)
FOREST_GREEN = ( 31, 162,  35)
BLUE         = (  0,   0, 255)
SKY_BLUE     = ( 39, 145, 251)
YELLOW       = (255, 255,   0)
ORANGE       = (255, 128,   0)
PURPLE       = (255,   0, 255)
CYAN         = (  0, 255, 255)
BLACK        = (  0,   0,   0)
NEAR_BLACK    = ( 19,  15,  48)
COMBLUE      = (233, 232, 255)
GOLD         = (255, 215,   0)

BGCOLOR = WHITE

SIZE_MULTIPLIER = 2.5
FUEGUITO_SIZE_MULTIPLIER = 2
BOWSER_SIZE_MULTIPLIER = 15
BRICK_SIZE_MULTIPLIER = 2.69
BACKGROUND_MULTIPLER = 2.679
GROUND_HEIGHT = SCREEN_HEIGHT - 62

NUM_OPERACIONES = 5

#MARIO FORCES
WALK_ACCEL = .15
RUN_ACCEL = 20
SMALL_TURNAROUND = .35

GRAVITY = 1.01
JUMP_GRAVITY = .31
JUMP_VEL = -10
FAST_JUMP_VEL = -12.5
MAX_Y_VEL = 11

MAX_RUN_SPEED = 800
MAX_WALK_SPEED = 6


#Mario States

STAND = 'standing'
WALK = 'walk'
JUMP = 'jump'
FALL = 'fall'
SMALL_TO_BIG = 'small to big'
BIG_TO_FIRE = 'big to fire'
BIG_TO_SMALL = 'big to small'
FLAGPOLE = 'flag pole'
WALKING_TO_CASTLE = 'walking to castle'
END_OF_LEVEL_FALL = 'end of level fall'


#GOOMBA Stuff

LEFT = 'left'
RIGHT = 'right'
JUMPED_ON = 'jumped on'
DEATH_JUMP = 'death jump'

#KOOPA STUFF

SHELL_SLIDE = 'shell slide'

#BRICK STATES

RESTING = 'resting'
BUMPED = 'bumped'

#COIN STATES
OPENED = 'opened'

#MUSHROOM STATES

REVEAL = 'reveal'
SLIDE = 'slide'

#COIN STATES

SPIN = 'spin'

#STAR STATES

BOUNCE = 'bounce'

#FIRE STATES

FLYING = 'flying'
BOUNCING = 'bouncing'
EXPLODING = 'exploding'

#Brick and coin box contents

MUSHROOM = 'mushroom'
STAR = 'star'
FIREFLOWER = 'fireflower'
SIXCOINS = '6coins'
COIN = 'coin'
LIFE_MUSHROOM = '1up_mushroom'

FIREBALL = 'fireball'

#LIST of ENEMIES

GOOMBA = 'goomba'
KOOPA = 'koopa'

#LEVEL STATES

FROZEN = 'frozen'
NOT_FROZEN = 'not frozen'
IN_CASTLE = 'in castle'
FLAG_AND_FIREWORKS = 'flag and fireworks'

#FLAG STATE
TOP_OF_POLE = 'top of pole'
SLIDE_DOWN = 'slide down'
BOTTOM_OF_POLE = 'bottom of pole'

#1UP score
ONEUP = '379'

#MAIN MENU CURSOR STATES
PLAYER1 = '1 player'
PLAYER2 = '2 player'

#OVERHEAD INFO STATES
MAIN_MENU = 'main menu'
LOAD_SCREEN = 'loading screen'
LEVEL = 'level'
GAME_OVER = 'game over'
FAST_COUNT_DOWN = 'fast count down'
END_OF_LEVEL = 'end of level'


#GAME INFO DICTIONARY KEYS
COIN_TOTAL = 'coin total'
SCORE = 'score'
TOP_SCORE = 'top score'
LIVES = 'lives'
CURRENT_TIME = 'current time'
LEVEL_STATE = 'level state'
CAMERA_START_X = 'camera start x'
MARIO_DEAD = 'mario dead'

#STATES FOR ENTIRE GAME
MAIN_MENU = 'main menu'
LOAD_SCREEN = 'load screen'
TIME_OUT = 'time out'
GAME_OVER = 'game over'
LEVEL1 = 'level1'

#SOUND STATEZ
NORMAL = 'normal'
STAGE_CLEAR = 'stage clear'
WORLD_CLEAR = 'world clear'
TIME_WARNING = 'time warning'
SPED_UP_NORMAL = 'sped up normal'
MARIO_INVINCIBLE = 'mario invincible'

# Tamaño de números y signos

X_PRIMERA_COLUMNA = 34
X_SEGUNDA_COLUMNA = 99
X_TERCERA_COLUMNA = 99
X_CUARTA_COLUMNA = 99
X_QUINTA_COLUMNA = 99
X_SEXTA_COLUMNA = 99
X_SEPTIMA_COLUMNA = 99
SIMBOLOS_WIDTH = 37

Y_PRIMERA_FILA = 34
Y_SEGUNDA_FILA = 99
SIMBOLOS_HEIGHT = 44

#cero
X_CERO = 47
Y_CERO = 34
ANCHO_CERO = 79 - 47 # 32
ALTO_CERO = 78 - 34  # 44

# UNO
X_UNO = 96
Y_UNO = 35
ANCHO_UNO = 122 - 96 # 26
ALTO_UNO = 78 - 35   # 43

# DOS
X_DOS = 139
Y_DOS = 35
ANCHO_DOS = 172 - 139 # 33
ALTO_DOS = 78 - 35    # 43

#TRES
X_TRES = 188
Y_TRES = 34
ANCHO_TRES = 218 - 188 # 30
ALTO_TRES = 78 - 34    # 44

# CUATRO
X_CUATRO = 237
Y_CUATRO = 35
ANCHO_CUATRO = 274 - 237 # 37
ALTO_CUATRO = 78 - 35    # 43

# CINCO
X_CINCO = 49
Y_CINCO = 99
ANCHO_CINCO = 78 - 49 # 29
ALTO_CINCO = 143 - 99 # 44

# SEIS
X_SEIS = 96
Y_SEIS = 99
ANCHO_SEIS = 125 - 96 # 29
ALTO_SEIS = 143 - 99  # 44

# SIETE
X_SIETE = 144
Y_SIETE = 100
ANCHO_SIETE = 174 - 144 # 30
ALTO_SIETE = 143 - 100  # 43

# OCHO
X_OCHO = 193
Y_OCHO = 100
ANCHO_OCHO = 221 - 193 # 28
ALTO_OCHO = 144 - 100  # 44

# NUEVE
X_NUEVE = 239
Y_NUEVE = 100
ANCHO_NUEVE = 266 - 239 # 27
ALTO_NUEVE = 143 - 100  # 43
"""

"""

SUMA = '+'
RESTA = '-'
MULTIPLICACION = '*' 
DIVISION = '/'

# SUMA
X_SUMA = 298
Y_SUMA = 41
ANCHO_SUMA = 333 - 298 # 35
ALTO_SUMA = 76 - 41  # 35

# RESTA
X_RESTA = 361
Y_RESTA = 53
ANCHO_RESTA = 396 - 361 # 35
ALTO_RESTA = 65 - 53  # 12

# MULTIPLICACION
X_MULTIPLICACION = 300
Y_MULTIPLICACION = 106
ANCHO_MULTIPLICACION = 331 - 300 # 31
ALTO_MULTIPLICACION = 137 - 106  # 31

# DIVISION
X_DIVISION = 363
Y_DIVISION = 104
ANCHO_DIVISION = 395 - 363 # 32
ALTO_DIVISION = 139 - 104  # 35