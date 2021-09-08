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
    def __init__(self, position: Collection, animation: Animation, game):
        super().__init__()
        self.game = game
        self.animation = animation
        self.image = animation.image
        self.rect = self.image.get_rect()
        self.rect.center = position


    def update(self):
       pass 


    def draw(self, surface=None):
        self.image = self.animation.image
        # Если указана другая поверхность, то рисовать на ней.
        if surface is None:
            self.game.screen.blit(self.image, self.rect)
        else: surface.draw(self.image, self.rect)
        self.animation.set_next_frame()


    def set_animation(self, animation: Animation):
        if animation is Animation:
            self.animation = animation
        else: raise TypeError("Это не アニメ！")