import pygame as pg
from player import Player
from animation import Animation
from world import Physics
from blocks import Block
from settings import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True
        self.setup_animations()
        self.setup_sprites()
        self.setup_physics()
    

    def run(self):
        self.loop()


    def loop(self):
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYUP 
                                            and event.key == pg.K_ESCAPE):
                    self.running = False

            self.update()
            self.draw()
            pg.display.flip()
    

    def draw(self):
        self.screen.fill((120, 80, 200))
        self.physics_group.draw(self.screen)
        self.static_group.draw(self.screen)


    def update(self):
        self.player.update()
        self.player2.update()
        self.physics.gravity()


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

    def setup_physics(self):
        self.physics = Physics(self)

    def setup_sprites(self):
        self.physics_group = pg.sprite.Group()
        self.static_group = pg.sprite.Group()
        # TODO: ???????????????? ???????????????? ???? Spritesheet
        self.player = Player(position=(200, 300), animation=self.basic_animation, game=self)
        self.player2 = Player(position=(300, 300), animation=self.basic_animation, game=self)
        
        block_img = pg.Surface((30, 30))
        self.block = Block((190, 500), block_img)
        
        self.physics_group.add(self.player)
        self.physics_group.add(self.player2)
        
        self.static_group.add(self.block)

if __name__ == '__main__':
    game = Game()
    game.run()