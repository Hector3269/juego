import pygame
import contantes
class personaje():
    def __init__(self, x, y, animaciones):
        self.flip = False
        self.animaciones = animaciones
        # imagen de la animacion que se esta nostrando
        self.frame_index = 0
        # la hora actual en milisegundos desde que inicio
        self.update_time = pygame.time.get_ticks()
        self.image = animaciones[self.frame_index]
        self.forma = self.image.get_rect()

        self.forma.center = (x, y)

    def movimiento(self, movimiento_x, movimiento_y):
        if movimiento_x < 0:
            self.flip = True
        if movimiento_x > 0:
            self.flip = False

        self.forma.x += movimiento_x
        self.forma.y += movimiento_y

    def update(self):
        cooldown_animacion =100
        self.image = self.animaciones[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
            self.frame_index =self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animaciones):
            self.frame_index = 0

    def dibujar(self, interfaz):
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        interfaz.blit(imagen_flip, self.forma)

        #pygame.draw.rect(interfaz,contantes.COLOR_PERSONAJE,self.forma,1)
