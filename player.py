import math
from typing import Collection
import pygame as pg
from enum import Flag, auto
from animation import Animation


class AnimationState(Flag):
    START = auto()
    IDLE = auto()
    WALK_LEFT = auto()
    WALK_RIGHT = auto()
    JUMP = auto()
    FALL = auto()


class Player(pg.sprite.Sprite):
    
    BASE_SPEED = 20

    def __init__(self, position: Collection, animation: Animation, game):
        super().__init__()
        self.game = game
        self.animation = animation
        try:
            self.image = animation.image 
        except AttributeError:
            raise TypeError("Animation should be an animation")
        self.rect = self.image.get_rect()
        self.rect.bottomleft = position
        self.on_ground = False


    def update(self):
       self.move()


    def draw(self, surface=None):
        self.image = self.animation.image
        # Если указана другая поверхность, то рисовать на ней.
        if surface is None:
            self.game.screen.blit(self.image, self.rect)
        else: surface.draw(self.image, self.rect)
        self.animation.set_next_frame()


    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            # если -speed*dt<1, тогда python округяет значение до -1 (пикселя)
            self.rect.x -= Player.BASE_SPEED*self.game.dt
        if keys[pg.K_RIGHT]:
            # если speed*dt<1, тогда python округяет значение до 0 (пикселей) и движения нет
            self.rect.x += math.ceil(Player.BASE_SPEED*self.game.dt)
        if keys[pg.K_SPACE]:
            self._jump()
    
    # def _jump(self):
    #     if self.on_ground:
    #         self.rect.y -= 1000*self.game.dt
    #         self.on_ground = False


    def set_animation(self, animation: Animation):
        if animation is Animation:
            self.animation = animation
        else: raise TypeError("Это не アニメ！")