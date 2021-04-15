__author__ = 'justinarmstrong'

import pygame as pg
from .. import setup
from .. import constants as c
from . import powerups
from . import coin


class Expresion(pg.sprite.Sprite):
    """Expresiones matemáticas incluyendo cuentas y resultados"""
    def __init__(self, x, y, expresion, name='expresion'):
        """Initialize the object"""
        pg.sprite.Sprite.__init__(self)
        self.sprite_sheet = setup.GFX['expresiones_images']

        self.frames = []
        self.frame_index = 0
        self.setup_frames(expresion)
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pg.mask.from_surface(self.image)
        self.name = name

    def get_image(self, x, y, width, height):
        """Extracts the image from the sprite sheet"""
        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        """
        image = pg.transform.scale(image,
                                   (int(rect.width*c.BRICK_SIZE_MULTIPLIER),
                                    int(rect.height*c.BRICK_SIZE_MULTIPLIER)))
        """
        return image


    def setup_frames(self, expresion):
        """Set the frames to a list"""

        image = self.get_image_expresion(expresion)

        """
        img_signo      = self.get_image_signo(operacion[1])

        img_operando_2 = self.get_image_numero(operacion[2])


        todo_junto = pg.Surface([img_operando_1.get_width() + 
                                 img_signo.get_width() + 
                                 img_operando_2.get_width(),
                                 c.NUMEROS_MAX_HEIGHT])
        todo_junto.blit(img_operando_1, (0, 0))
        todo_junto.blit(img_signo, (img_operando_1.get_width(), 20))
        todo_junto.blit(img_operando_2, (img_operando_1.get_width() + img_signo.get_width(), 0))
        """

        self.frames.append(image)
        
    
    def get_image_expresion(self, expresion):

        anchura_acumulada = 0

        #Damos una primera vuelta para calcular la anchura acumulada
        for i in str(expresion):
            if i == str(0):
                image_aux = self.get_image(c.X_CERO, c.Y_CERO, c.ANCHO_CERO, c.ALTO_CERO)
            elif i == str(1):
                image_aux = self.get_image(c.X_UNO, c.Y_UNO, c.ANCHO_UNO, c.ALTO_UNO)
            elif i == str(2):
                image_aux = self.get_image(c.X_DOS, c.Y_DOS, c.ANCHO_DOS, c.ALTO_DOS)
            elif i == str(3):
                image_aux = self.get_image(c.X_TRES, c.Y_TRES, c.ANCHO_TRES, c.ALTO_TRES)
            elif i == str(4):
                image_aux = self.get_image(c.X_CUATRO, c.Y_CUATRO, c.ANCHO_CUATRO, c.ALTO_CUATRO)
            elif i == str(5):
                image_aux = self.get_image(c.X_CINCO, c.Y_CINCO, c.ANCHO_CINCO, c.ALTO_CINCO)
            elif i == str(6):
                image_aux = self.get_image(c.X_SEIS, c.Y_SEIS, c.ANCHO_SEIS, c.ALTO_SEIS)
            elif i == str(7):
                image_aux = self.get_image(c.X_SIETE, c.Y_SIETE, c.ANCHO_SIETE, c.ALTO_SIETE)
            elif i == str(8):
                image_aux = self.get_image(c.X_OCHO, c.Y_OCHO, c.ANCHO_OCHO, c.ALTO_OCHO)
            elif i == str(9):
                image_aux = self.get_image(c.X_NUEVE, c.Y_NUEVE, c.ANCHO_NUEVE, c.ALTO_NUEVE)
            elif i == c.SUMA:
                image_aux = self.get_image(c.X_SUMA, c.Y_SUMA, c.ANCHO_SUMA, c.ALTO_SUMA)
            elif i == c.RESTA:
                image_aux = self.get_image(c.X_RESTA, c.Y_RESTA, c.ANCHO_RESTA, c.ALTO_RESTA)
            elif i == c.MULTIPLICACION:
                image_aux = self.get_image(c.X_MULTIPLICACION, c.Y_MULTIPLICACION, c.ANCHO_MULTIPLICACION, c.ALTO_MULTIPLICACION)
            elif i == c.DIVISION:
                image_aux = self.get_image(c.X_DIVISION, c.Y_DIVISION, c.ANCHO_DIVISION, c.ALTO_DIVISION)

            anchura_acumulada += image_aux.get_width()        



        image = pg.Surface([anchura_acumulada,c.SIMBOLOS_HEIGHT])

        anchura_aux = 0
        
        for i in str(expresion):
            if i == str(0):
                image_aux = self.get_image(c.X_CERO, c.Y_PRIMERA_FILA, c.ANCHO_CERO, c.SIMBOLOS_HEIGHT)
            elif i == str(1):
                image_aux = self.get_image(c.X_UNO, c.Y_PRIMERA_FILA, c.ANCHO_UNO, c.SIMBOLOS_HEIGHT)
            elif i == str(2):
                image_aux = self.get_image(c.X_DOS, c.Y_PRIMERA_FILA, c.ANCHO_DOS, c.SIMBOLOS_HEIGHT)
            elif i == str(3):
                image_aux = self.get_image(c.X_TRES, c.Y_PRIMERA_FILA, c.ANCHO_TRES, c.SIMBOLOS_HEIGHT)
            elif i == str(4):
                image_aux = self.get_image(c.X_CUATRO, c.Y_PRIMERA_FILA, c.ANCHO_CUATRO, c.SIMBOLOS_HEIGHT)
            elif i == str(5):
                image_aux = self.get_image(c.X_CINCO, c.Y_SEGUNDA_FILA, c.ANCHO_CINCO, c.SIMBOLOS_HEIGHT)
            elif i == str(6):
                image_aux = self.get_image(c.X_SEIS, c.Y_SEGUNDA_FILA, c.ANCHO_SEIS, c.SIMBOLOS_HEIGHT)
            elif i == str(7):
                image_aux = self.get_image(c.X_SIETE, c.Y_SEGUNDA_FILA, c.ANCHO_SIETE, c.SIMBOLOS_HEIGHT)
            elif i == str(8):
                image_aux = self.get_image(c.X_OCHO, c.Y_SEGUNDA_FILA, c.ANCHO_OCHO, c.SIMBOLOS_HEIGHT)
            elif i == str(9):
                image_aux = self.get_image(c.X_NUEVE, c.Y_SEGUNDA_FILA, c.ANCHO_NUEVE, c.SIMBOLOS_HEIGHT)
            elif i == c.SUMA:
                image_aux = self.get_image(c.X_SUMA, c.Y_PRIMERA_FILA, c.ANCHO_SUMA, c.SIMBOLOS_HEIGHT)
            elif i == c.RESTA:
                image_aux = self.get_image(c.X_RESTA, c.Y_PRIMERA_FILA, c.ANCHO_RESTA, c.SIMBOLOS_HEIGHT)
            elif i == c.MULTIPLICACION:
                image_aux = self.get_image(c.X_MULTIPLICACION, c.Y_SEGUNDA_FILA, c.ANCHO_MULTIPLICACION, c.SIMBOLOS_HEIGHT)
            elif i == c.DIVISION:
                image_aux = self.get_image(c.X_DIVISION, c.Y_SEGUNDA_FILA, c.ANCHO_DIVISION, c.SIMBOLOS_HEIGHT)

            image.blit(image_aux, (anchura_aux, 0))
            anchura_aux += image_aux.get_width()
            
        
        return image