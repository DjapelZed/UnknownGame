import pygame as pg


class Animation:
    """
    surfaces - кадры для анимации, список объектов типа pygame.Surface
    speed - скорость анимации. Чем выше, тем быстрее.
    
    Класс анимации игровых объектов.
    Анимация циклична: после последнего кадра, следует первый.

    ! ! ! В игровом объекте pygame.Sprite присваивать атрибуту image значение Animation.image
    ! ! ! Вызывать функцию set_next_frame при каждом обновлении кадра.
    """
    def __init__(self, surfaces: dict, speed=20):
        self.images = surfaces
        self.image = surfaces[0]
        self.rect = self.image.get_rect()
        self.animation_speed = speed
        self._tick = 0
        self._absolute_last_frame_time = pg.time.get_ticks()

    def set_next_frame(self):
        self.image = self.images[self._tick]
        if pg.time.get_ticks() - self._absolute_last_frame_time > 600 / self.animation_speed:
            self._tick += 1
            self._absolute_last_frame_time = pg.time.get_ticks()
        if self._tick >= len(self.images): self._tick = 0
