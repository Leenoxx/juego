class Button:
    def __init__(self, x, y, imagen):
        self.__imagen = imagen  # Imágen que insertamos
        self.__rect = self.__imagen.get_rect()
        self.rect.topleft = (x, y)  # Definimos la posición

    def draw(self, surface):
        surface.blit(self.__imagen, (self.rect.x, self.rect.y))

    @property
    def imagen(self):
        return self.__imagen

    @property
    def rect(self):
        return self.__rect
