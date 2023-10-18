import pygame
from renderers.utils import render_image, render_tiles
from renderers.entities import PhysicsEntity
from renderers.tilemap import Tilemap
import sys
#imports

class Game:
#class to easily replicate objects
    def __init__(self):
    #init script to load assets and load window 
        pygame.init()

        pygame.display.set_caption("Halloween Rush")
        self.window = pygame.display.set_mode((640,480))
        self.display = pygame.Surface((320, 240))
        self.clock = pygame.time.Clock()
        
        self.move = [False, False]
        
        self.assets = {
            "Player": render_image("skelo-static/skelo-warrior.png"),
            "decor": render_tiles("tiles/decor"),
            "ground": render_tiles("tiles/ground")
        }
        
        self.player = PhysicsEntity(self, 'Player', (50, 50), (8, 15))

        self.tilemap = Tilemap(self)
        
    
    def run(self):
    #runs game (loops event listener) and updates display while limiting to 60fps
        while True:
            self.display.fill((142,142,142))

            self.tilemap.render(self.display)
            
            self.player.update(self.tilemap, (self.move[1] - self.move[0], 0))
            self.player.render(self.display)
            
            print(self.tilemap.physics_rect_around(self.player.pos))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.move[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.move[1] = True
                    
                    if event.key == pygame.K_a:
                        self.move[0] = True
                    if event.key == pygame.K_d:
                        self.move[1] = True
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.move[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.move[1] = False
                    
                    if event.key == pygame.K_a:
                        self.move[0] = False
                    if event.key == pygame.K_d:
                        self.move[1] = False
            
            self.window.blit(pygame.transform.scale(self.display, self.window.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)
            
Game().run()