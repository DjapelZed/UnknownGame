import pygame as pg


class Physics:

    G = 10

    def __init__(self, game):
        self.game = game
        self.objects = game.physics_group
        self.last_time = pg.time.get_ticks()
        self.acceleration = 60


    def gravity(self):
        for object in self.objects:
            if pg.sprite.spritecollide(object, self.game.static_group, False):
                object.falltime = 0
                self.acceleration = 0
                object.on_ground = True
            else: self.acceleration = 60
            object.rect.y += Physics.G*self.acceleration*self.game.dt
