import pygame
import contantes
from Personaje import personaje
from weapon import Weapons

pygame.init()
ventana = pygame.display.set_mode((contantes.ANCHO_VENTANA,
                                   contantes.ALTO_VENTANA))
pygame.display.set_caption("matgame")


def escalar_img(image,scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image,(w*scale,h*scale))
    return nueva_imagen

# importar imagenes para el personaje
animasiones = []
for i in range(7):
    img = pygame.image.load(f"Assets//imagen//caracteres//Jugador//jugador_{i}.png ")
    img = escalar_img(img,contantes.SCALA_PERSONAJE)
    animasiones.append(img)
# arma
imagen_pistola = pygame.image.load(f"Assets//imagen//weapons//pistola.png")
imagen_pistola = escalar_img(imagen_pistola,contantes.SCALA_ARMA)

# balas
imagen_bala = pygame.image.load(f"Assets//imagen//weapons//bala.png.")
imagen_bala = escalar_img(imagen_bala, contantes.SCALA_ARMA)

# crea un jugador de la clase personaje
Jugador = personaje(50, 50, animasiones)

# crear un arma de la clase weapon
pistola = Weapons(imagen_pistola, imagen_bala)

# crear ungrupo de Sprite
grupo_bala = pygame.sprite.Group()

# Definir las variables de movimiento del jugador
mover_arriba = False
mover_abajo = False
mover_derecha = False
mover_izquierda = False

# Controlar los cuadros por segundo
reloj = pygame.time.Clock()

run = True
while run:
    # Que vaya a 60 FPS fotogramas por segundo
    reloj.tick(contantes.FPS)

    ventana.fill(contantes.COLOR_BG)

    # Calcular el movimiento del jugador
    movimiento_x = 0
    movimiento_y = 0

    if mover_derecha:
        movimiento_x = contantes.VELOSIDAD
    if mover_izquierda:
        movimiento_x = contantes.VELOSIDAD2
    if mover_arriba:
        movimiento_y = contantes.VELOSIDAD2
    if mover_abajo:
        movimiento_y = contantes.VELOSIDAD
    # mover jugador
    Jugador.movimiento(movimiento_x, movimiento_y)

    # actualiza estado de jugador
    Jugador.update()

    # acctualiza estado del arma
    bala = pistola.update(Jugador)
    if bala:
        grupo_bala.add(bala)
    for bala in grupo_bala:
        bala.update()
    print(grupo_bala)

    # Dibujar al jugador
    Jugador.dibujar(ventana)

    # dibujar bala
    for bala in grupo_bala:
        bala.dibujar(ventana)

    # Dibujar al arma
    pistola.dibujar(ventana)

    for event in pygame.event.get():
        # Método de cierre del juego
        if event.type == pygame.QUIT:
            run = False
        # Función de movimiento del personaje
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True

        # Para cuando se suelte la tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False

    pygame.display.update()

pygame.quit()