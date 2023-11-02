import pygame
from renderers.utils import render_image, render_tiles, Animation
from renderers.entities import PhysicsEntity, Player, Enemy
from renderers.tilemap import Tilemap
import time
import sys
from random import randint
#imports


class Game:
#class to easily replicate objects
    def __init__(self):
    #init script to load assets and load window 
        pygame.init()

        icon = pygame.image.load("dress_code-comp/code/sprites/icon.png")
        self.font = pygame.font.Font("dress_code-comp/code/ARCADECLASSIC.ttf")
        


        pygame.display.set_icon(icon)
        pygame.display.set_caption("Halloween Rush")
        self.window = pygame.display.set_mode((640,480))
        self.display = pygame.Surface((320, 240))
        self.clock = pygame.time.Clock()
        
        self.move = [False, False]
        self.ghost_move = [False, False]
        
        self.assets = {
            "Player": render_image("skelo-static/skelo-warrior.png"),
            "decor": render_tiles("tiles/decor"),
            "ground": render_tiles("tiles/ground"),
            "bg": render_image("background.png"),
            "platform": render_tiles("tiles/platform"),
            "Player/idle": Animation(render_tiles('skelo-idle'), images_dur=7),
            "Player/jump": Animation(render_tiles("skelo-jump"), images_dur=15),
            "ghost/idle": Animation(render_tiles("ghost"), images_dur=7),
            "ectoplasm": Animation(render_tiles("projectile"))
        }
        
        self.player = Player(self, (50, 50), (32, 30))
        self.ghost = Enemy(self, (randint(50, 340), 50), (32, 30))

        self.frames_passed = 0
        self.seconds_passed = 0

        self.tilemap = Tilemap(self)
        
        self.enemies = []

        self.passed = 0

        self.lost = False

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
            #self.ghost.update(self.tilemap)
            #self.ghost.render(self.display, offset = render_scroll)


            for enemy in self.enemies:
                self.ghost_move = [False, False]

                move_left = randint(0, 1)
                move_right = randint(0, 1)

                if move_left == 0:
                    self.ghost_move[0] = False
                else:
                    self.ghost_move[0] = True

                if move_right == 0:
                    self.ghost_move[1] = False
                else:
                    self.ghost_move[1] = True

                enemy.update(self.tilemap, (self.ghost_move[1] - self.ghost_move[0], 0))
                enemy.render(self.display, offset = render_scroll)

                player_rect = self.player.rect()
                enemy_rect = enemy.rect()

                if player_rect.colliderect(enemy_rect):
                    self.lost = True

            if self.seconds_passed % 10 == 0:
                new_enemy = Enemy(self, (randint(70, 340), 50), (32, 30))
                self.enemies.append(new_enemy)


            text = self.font.render(f"Time Survived {int(self.seconds_passed)}", True, (240, 240, 240))
            text_rect = text.get_rect()

            text_rect.topleft = (0, 0)

            self.display.blit(text, (0,0))

            if self.lost:
                lost = self.font.render(f"You  survived  for  {int(self.seconds_passed)} seconds", True, (255, 0, 10))
                self.display.blit(lost, self.display.get_rect().center)

                if self.passed == 60:
                    time.sleep(3)
                    sys.exit()
                
            if self.lost:
                self.passed += 1

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
                        if int(self.player.pos[1]) == 146:
                            self.player.velocity[1] = -4.5
                    if event.key == pygame.K_w:
                        if int(self.player.pos[1]) == 146:
                            self.player.velocity[1] = -4.5
                        
                    if event.key == pygame.K_SPACE:
                        if int(self.player.pos[1]) == 146:
                            self.player.velocity[1] = -4.5
                        
            
            if int(self.player.pos[1]) > 170:
                self.lost = True
            
                 
            
            self.window.blit(pygame.transform.scale(self.display, self.window.get_size()), (0, 0))
            pygame.display.update()
            if not self.lost:
                self.frames_passed += 1
            self.clock.tick(60)
            self.seconds_passed = self.frames_passed / 60
            
            
Game().run()
