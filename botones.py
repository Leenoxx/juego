class Button:
    def __init__(self, x, y, imagen):
        self.imagen = imagen  # Imágen que insertamos
        self.rect = self.imagen.get_rect()
        self.rect.topleft = (x, y)  # Definimos la posición

    def draw(self, surface):
        surface.blit(self.imagen, (self.rect.x, self.rect.y))
