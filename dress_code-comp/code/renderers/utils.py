import pygame
import os

BASE_IMG_PATH = 'dress_code-comp/code/sprites/'

def render_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path)
    return img

def render_tiles(path):
    images = []
    for img_name in os.listdir(BASE_IMG_PATH + path):
        images.append(render_image(f"{path}/{img_name}"))
    return images

class Animation:
    def __init__(self, images, images_dur=5, loop=True):
        self.images = images
        self.loop = loop
        self.img_duration = images_dur
        self.done = False
        self.frame = 0

    def copy(self):
        return Animation(self.images, self.img_duration, self.loop)
    
    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (self.img_duration * len(self.images))
        else:
            self.frame = min(self.frame + 1, self.img_duration * len(self.images) -1)
            if self.frame >= self.img_duration * len(self.images) - 1:
                self.done = True

    def img(self):
        return self.images[int(self.frame / self.img_duration)]