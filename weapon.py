import pygame
import contantes
import math
class Weapons():
    def __init__(self, image, imagen_bala):
        self.imagen_bala = imagen_bala
        self.imagen_original = image
        self.angulo = 0
        self.imagen = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.forma = self.imagen.get_rect()
        self.dispara = False
        self.ultimo_disparo = pygame.time.get_ticks()
    def update(self, personaje):
        disparo_cooldowon = contantes.COOLDOWON_BALAS
        bala = None
        self.forma.center = personaje.forma.center

        if personaje.flip == False:
            self.forma.x = self.forma.x + personaje.forma.width/6
            self.rotar_arma(False)


        if personaje.flip == True:
            self.forma.x = self.forma.x - personaje.forma.width/6
            self.rotar_arma(True)

        # mover arma con el muse
        mouse_pos = pygame.mouse.get_pos()
        diferncia_x = mouse_pos[0] - self.forma.centerx
        diferncia_y = -mouse_pos[1] - self.forma.centery
        self.angulo = math.degrees(math.atan2(diferncia_y, diferncia_x))


        if pygame.mouse.get_pressed()[0] and self.dispara == False and (pygame.time.get_ticks()-self.ultimo_disparo >=  disparo_cooldowon):
            bala = Bullet(self.imagen_bala, self.forma.centerx, self.forma.centery, self.angulo)
            self.dispara = True
            self.ultimo_disparo = pygame.time.get_ticks()
        # resetear el clik  del mouse
        if pygame.mouse.get_pressed()[0] == False:
            self.dispara = False
        return bala


    def rotar_arma(self, rotar):
        if rotar == True:
            imagen_flip = pygame.transform.flip(self.imagen_original,
                                                True, False)
            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)
        else:
            imagen_flip = pygame.transform.flip(self.imagen_original,
                                                False, False)
            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)

    def dibujar(self, interfaz):
        self.imagen = pygame.transform.rotate(self.imagen,
                                              self.angulo)
        interfaz.blit(self.imagen, self.forma)
        # pygame.draw.rect(interfaz,contantes.COLOR_ARMA,self.forma,1)
class Bullet (pygame.sprite.Sprite):
    def __init__(self, image, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.imagen_original = image
        self.angulo = angle
        self.image = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        # calcular la velocidad
        self.delta_x = math.cos(math.radians(self.angulo)) * contantes.VELOSIDAD_BALA
        self.delta_y = -math.sin(math.radians(self.angulo)) * contantes.VELOSIDAD_BALA
    def update(self):
        self.rect.x += self.delta_x
        self.rect.y += self.delta_y

        # ver si las valas ya salieron de pantalla
        if self.rect.right < 0 or self.rect.left > contantes.ALTO_VENTANA or self.rect.top > contantes.ALTO_VENTANA:
            self.kill()
    def dibujar (self, interfaz):
        interfaz.blit(self.image, (self.rect.centerx,
                      self.rect.centery - int(self.image.get_height()*2)))