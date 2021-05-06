from data import constants as c
"""
Con este programa comprobaremos el código recibido

"""

codigo = input('Introduce el código: ')

codigo_base_decimal = int(codigo, 16)

print('El código corresponde al nivel '+ str(codigo_base_decimal%c.NUM_MAX_NIVELES))