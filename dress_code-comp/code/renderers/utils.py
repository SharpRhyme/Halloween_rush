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