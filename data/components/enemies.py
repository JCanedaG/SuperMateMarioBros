__author__ = 'justinarmstrong'


import pygame as pg
from .. import setup
from .. import constants as c


class Enemy(pg.sprite.Sprite):
    """Base class for all enemies (Goombas, Koopas, etc.)"""
    def __init__(self):
        pg.sprite.Sprite.__init__(self)


    def setup_enemy(self, x, y, direction, name, setup_frames, monstruo_principal=False, fueguito=False, nivel=1):
        """Sets up various values for enemy"""
        self.sprite_sheet = setup.GFX['smb_enemies_sheet']
        self.frames = []
        self.frame_index = 0
        self.animate_timer = 0
        self.death_timer = 0
        self.gravity = 1.5
        self.state = c.WALK

        self.name = name
        self.direction = direction
        self.monstruo_principal = monstruo_principal
        self.fueguito = fueguito
        setup_frames()

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x #if not monstruo_principal else 0
        self.rect.bottom = y #if not monstruo_principal else c.GROUND_HEIGHT
        self.set_velocity(monstruo_principal=self.monstruo_principal, nivel=nivel)


    def set_velocity(self, monstruo_principal=False, nivel=1):
        """Sets velocity vector based on direction"""
        if self.direction == c.LEFT:
            self.x_vel = -2
        elif self.direction == c.RIGHT:
            if monstruo_principal:
                # Para la velocidad de Bowser, 1.5 es muy lento, y 4 es muy rápido
                # Hacemos para que se llegue a velocidad 4 al nivel 50
                self.x_vel = 1.5 + 2.5*(nivel/50)
        else:
            self.x_vel = 0

        self.y_vel = 0

    def get_image(self, x, y, width, height, multiplier=c.SIZE_MULTIPLIER):
        """Get the image frames from the sprite sheet"""
        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)


        image = pg.transform.scale(image,
                                   (int(rect.width*multiplier),
                                    int(rect.height*multiplier)))
        return image


    def handle_state(self):
        """Enemy behavior based on state"""
        if self.state == c.WALK:
            self.walking()
        elif self.state == c.FALL:
            self.falling()
        elif self.state == c.JUMPED_ON:
            self.jumped_on()
        elif self.state == c.SHELL_SLIDE:
            self.shell_sliding()
        elif self.state == c.DEATH_JUMP:
            self.death_jumping()


    def walking(self):
        """Default state of moving sideways"""
        if (self.current_time - self.animate_timer) > 125:
            if self.frame_index == 0:
                self.frame_index += 1
            elif self.frame_index == 1:
                self.frame_index = 0

            self.animate_timer = self.current_time


    def falling(self):
        """For when it falls off a ledge"""
        if self.y_vel < 10:
            self.y_vel += self.gravity


    def jumped_on(self):
        """Placeholder for when the enemy is stomped on"""
        pass


    def death_jumping(self):
        """Death animation"""
        self.rect.y += self.y_vel
        self.rect.x += self.x_vel
        self.y_vel += self.gravity

        if self.rect.y > 600:
            self.kill()


    def start_death_jump(self, direction):
        """Transitions enemy into a DEATH JUMP state"""
        self.y_vel = -8
        if direction == c.RIGHT:
            self.x_vel = 2
        else:
            self.x_vel = -2
        self.gravity = .5
        self.frame_index = 3
        self.image = self.frames[self.frame_index]
        self.state = c.DEATH_JUMP


    def animation(self):
        """Basic animation, switching between two frames"""
        self.image = self.frames[self.frame_index]


    def update(self, game_info, *args):
        """Updates enemy behavior"""
        self.current_time = game_info[c.CURRENT_TIME]
        self.handle_state()
        self.animation()




class Goomba(Enemy):

    def __init__(self, y=c.GROUND_HEIGHT, x=0, direction=c.LEFT, name='goomba'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames)


    def setup_frames(self):
        """Put the image frames in a list to be animated"""

        self.frames.append(
            self.get_image(0, 4, 16, 16))
        self.frames.append(
            self.get_image(30, 4, 16, 16))
        self.frames.append(
            self.get_image(61, 0, 16, 16))
        self.frames.append(pg.transform.flip(self.frames[1], False, True))


    def jumped_on(self):
        """When Mario squishes him"""
        self.frame_index = 2

        if (self.current_time - self.death_timer) > 500:
            self.kill()



class Koopa(Enemy):

    def __init__(self, y=c.GROUND_HEIGHT, x=0, direction=c.LEFT, name='koopa'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames)


    def setup_frames(self):
        """Sets frame list"""
        self.frames.append(
            self.get_image(150, 0, 16, 24))
        self.frames.append(
            self.get_image(180, 0, 16, 24))
        self.frames.append(
            self.get_image(360, 5, 16, 15))
        self.frames.append(pg.transform.flip(self.frames[2], False, True))


    def jumped_on(self):
        """When Mario jumps on the Koopa and puts him in his shell"""
        self.x_vel = 0
        self.frame_index = 2
        shell_y = self.rect.bottom
        shell_x = self.rect.x
        self.rect = self.frames[self.frame_index].get_rect()
        self.rect.x = shell_x
        self.rect.bottom = shell_y


    def shell_sliding(self):
        """When the koopa is sliding along the ground in his shell"""
        if self.direction == c.RIGHT:
            self.x_vel = 10
        elif self.direction == c.LEFT:
            self.x_vel = -10



class Fueguito(Enemy):

    def __init__(self, y=0, x=0, direction=None, name='fueguito'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames, fueguito=True)


    def setup_frames(self):
        """Sets frame list"""
        self.frames.append(
            self.get_image(364, 179, 8, 34, multiplier=c.FUEGUITO_SIZE_MULTIPLIER))
        self.frames.append(
            self.get_image(377, 179, 8, 34, multiplier=c.FUEGUITO_SIZE_MULTIPLIER))
        self.frames.append(
            self.get_image(420, 184, 16, 16, multiplier=c.FUEGUITO_SIZE_MULTIPLIER))
        self.frames.append(
            self.get_image(392, 185, 12, 12, multiplier=c.FUEGUITO_SIZE_MULTIPLIER))


class Bowser(Enemy):

    def __init__(self, y=c.GROUND_HEIGHT, x=0, direction=c.RIGHT, name='bowser', nivel=1):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames, monstruo_principal=True, nivel=nivel)


    def setup_frames(self):
        """Sets frame list"""
        self.frames.append(
            self.get_image(162, 211, 32, 32, multiplier=c.BOWSER_SIZE_MULTIPLIER))
        self.frames.append(
            self.get_image(202, 211, 32, 32, multiplier=c.BOWSER_SIZE_MULTIPLIER))

class Luisal(Enemy):

    def __init__(self, y=c.GROUND_HEIGHT, x=0, direction=c.LEFT, name='luisal'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames)


    def setup_frames(self):
        """Sets frame list"""
        self.frames.append(
            self.get_image(150, 0, 16, 24))
        self.frames.append(
            self.get_image(180, 0, 16, 24))
        self.frames.append(
            self.get_image(360, 5, 16, 15))
        self.frames.append(pg.transform.flip(self.frames[2], False, True))


    def jumped_on(self):
        """When Mario jumps on the Koopa and puts him in his shell"""
        self.x_vel = 0
        self.frame_index = 2
        shell_y = self.rect.bottom
        shell_x = self.rect.x
        self.rect = self.frames[self.frame_index].get_rect()
        self.rect.x = shell_x
        self.rect.bottom = shell_y


    def shell_sliding(self):
        """When the koopa is sliding along the ground in his shell"""
        if self.direction == c.RIGHT:
            self.x_vel = 10
        elif self.direction == c.LEFT:
            self.x_vel = -10



















