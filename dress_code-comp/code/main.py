import pygame
from renderers.utils import render_image, render_tiles, Animation
from renderers.entities import PhysicsEntity, Player
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
            "ground": render_tiles("tiles/ground"),
            "bg": render_image("background.png"),
            "platform": render_image("platform.png"),
            "Player/idle": Animation(render_tiles('skelo-idle'), images_dur=7),
            "Player/jump": Animation(render_tiles("skelo-jump"), images_dur=8)
        }
        
        self.player = Player(self, (50, 50), (32, 30))

        self.tilemap = Tilemap(self)

        self.scroll = [0, 0]
        
    
    def run(self):
    #runs game (loops event listener) and updates display while limiting to 60fps
        while True:
            self.display.blit(self.assets["bg"], (0, 0))

            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

            self.tilemap.render(self.display, offset = render_scroll)
            
            self.player.update(self.tilemap, (self.move[1] - self.move[0], 0))
            self.player.render(self.display, offset = render_scroll)

            
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
                    
                    if event.key == pygame.K_UP:
                        self.player.velocity[1] = -3
                    if event.key == pygame.K_w:
                        self.player.velocity[1] = -3
                    if event.key == pygame.K_SPACE:
                        self.player.velocity[1] = -3
            
            self.window.blit(pygame.transform.scale(self.display, self.window.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)
            
Game().run()