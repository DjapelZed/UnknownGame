import pygame as pg
from player import Player
from animation import Animation
from settings import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True
        self.setup_animations()
        self.setup_sprites()
    

    def run(self):
        self.loop()


    def loop(self):
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            self.update()
            self.draw()
            pg.display.flip()
    

    def draw(self):
        self.screen.fill((120, 80, 200))
        self.player.draw()


    def update(self):
        pass


    def setup_animations(self):
        def get_surfaces(paths):
            surfaces = []
            for path in paths:
                surfaces.append(pg.image.load(path))
            return surfaces

        def DEV_get_rect_surfaces():
            return pg.Surface((28,60)), pg.Surface((28,56)), pg.Surface((28,54)), pg.Surface((28,56))


        # START
        image_paths = []
        surfaces = DEV_get_rect_surfaces() if True else get_surfaces(image_paths)
        self.basic_animation = Animation(surfaces, speed=ANIMATION_SPEED)

        # # IDLE
        # image_paths = []
        # surfaces = get_surfaces(image_paths)
        # self.idle_animation = Animation(surfaces)

        # # WALK
        # image_paths = []
        # surfaces = get_surfaces(image_paths)
        # self.walk_animation = Animation(surfaces)
        
        # # RUN
        # image_paths = []
        # surfaces = get_surfaces(image_paths)
        # self.run_animation = Animation(surfaces)
        
        # # FALL
        # image_paths = []
        # surfaces = get_surfaces(image_paths)
        # self.fall_animation = Animation(surfaces)

        # # JUMP
        # image_paths = []
        # surfaces = get_surfaces(image_paths)
        # self.jump_animation = Animation(surfaces)


    def setup_sprites(self):
        # TODO: Загрузка спрайтов из Spritesheet
        self.player = Player(position=(200, 300), animation=self.basic_animation, game=self)


if __name__ == '__main__':
    game = Game()
    game.run()