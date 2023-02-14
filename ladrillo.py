import pygame


class Brick:
    def __init__(self, pos_x, pos_y, imagen_ladrillo):
        self.__image = pygame.image.load(imagen_ladrillo)
        self.__rect = self.__image.get_rect()
        self.__rect.move_ip(pos_x, pos_y)

    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect
