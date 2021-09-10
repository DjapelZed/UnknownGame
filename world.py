import pygame as pg


class Physics:
    G = 10
    def __init__(self, objects: dict):
        self.objects = objects

    def gravity(self):
        for object in self.objects:
            object.rect.y += Physics.G

