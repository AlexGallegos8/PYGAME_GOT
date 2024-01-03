from operator import truediv
import pygame
import sys
import random
#se inicia el pygame
pygame.init()

#constante del ancho y alto
ANCHO_VENTANA = 1280
ALTO_VENTANA = 720

#canvas
canvas = 0

#colores
COLOR_NEGRO =  (0,0,0)
COLOR_BLANCO = (255,255,255)
COLOR_AZUL = (0,0,255)

#obstaculo
obstaculo_1_velocidad = 10
obstaculo1_alto = 100
obstaculo1_ancho = 100
obstaculo1_x = 200
obstaculo1_y = 100
obstaculo1_inicio_x = 200
obstaculo_1_inicio_y = 100

#obstaculo
obstaculo_2_velocidad = 10
obstaculo2_alto = 100
obstaculo2_ancho = 100
obstaculo2_x = 600
obstaculo2_y = 100
obstaculo2_inicio_x = 600
obstaculo_2_inicio_y = 100

#obstaculo
obstaculo_3_velocidad = 10
obstaculo3_alto = 100
obstaculo3_ancho = 100
obstaculo3_x = 1000
obstaculo3_y = 100
obstaculo3_inicio_x = 1000
obstaculo_3_inicio_y = 100

#dragon
dragon_1_velocidad = 20
dragon1_alto = 300
dragon1_ancho = 600
dragon1_x = random.randint(0,ANCHO_VENTANA)
dragon1_y = 0
dragon1_inicio_x = random.randint(0,ANCHO_VENTANA)
dragon1_inicio_y = 0


#condicion de derrota
derrota = False

#fondo 
fondo1 = pygame.image.load("imagenes/fondo_nivel_2.jpg")

#configurar fondo
fondo1 = pygame.transform.scale(fondo1,(ANCHO_VENTANA,ALTO_VENTANA))

#personaje
personaje1 = pygame.image.load("imagenes/personaje1.png")

#configurar personaje
personaje1 = pygame.transform.scale(personaje1,(75,106))



#posiciones del personaje
personaje1x = (ANCHO_VENTANA - personaje1.get_width()) // 2
personaje1y = ALTO_VENTANA - personaje1.get_height()
#se crea una pantalla
canvas = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("The Throne of Ice and Fire")

#movimiento
movimiento = 0

#tiempo
tiempo = pygame.time.Clock()

def persona1funcion(posx,posy):
    canvas.blit(personaje1,(posx,posy))

def obstaculofuncion(ruta,x,y,ancho,alto):
    obstaculo1 = pygame.image.load(ruta)
    obstaculo1 = pygame.transform.scale(obstaculo1,(ancho,alto))
    canvas.blit(obstaculo1,(x,y))

def colision():
    if obstaculo_1_inicio_y + obstaculo1_alto > personaje1y:
        if (personaje1x + personaje1.get_width() > obstaculo1_inicio_x and
            personaje1x < obstaculo1_inicio_x + obstaculo1_ancho):
            return True
        elif (personaje1x + personaje1.get_width() > obstaculo2_inicio_x and
            personaje1x < obstaculo2_inicio_x + obstaculo2_ancho):
            return True
        elif (personaje1x + personaje1.get_width() > obstaculo3_inicio_x and
            personaje1x < obstaculo3_inicio_x + obstaculo3_ancho):
            return True
    return False

def mostrar_ventana(texto,valor):
    mensaje = pygame.font.Font(None, 36).render(texto, True, (255, 255, 255))
    mensaje_rect = mensaje.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2))
    canvas.blit(mensaje, mensaje_rect)
    pygame.display.flip()
    esperando_tecla = True
    while esperando_tecla:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and valor == 0:
                esperando_tecla = False
            elif event.type == pygame.KEYDOWN and valor ==1:
                pygame.quit()
                sys.exit(0)

mostrar_ventana("Bienvenid@ ingresa cualquier tecla para iniciar",0)
#bucle principal del juego
while not derrota:
    #bucle de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            derrota = True
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                movimiento = -10
            if evento.key == pygame.K_RIGHT:
                movimiento = 10
        if evento.type == pygame.KEYUP:
            if (evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT):
                movimiento = 0
    if personaje1x + movimiento >= 0 and personaje1x + movimiento + personaje1.get_width() < ANCHO_VENTANA:
        personaje1x = personaje1x + movimiento
    elif personaje1x + movimiento + personaje1.get_width() > ANCHO_VENTANA:
        mostrar_ventana("Ganaste Ingresa cualquier tecla para salir",1)
    obstaculo_1_inicio_y += obstaculo_1_velocidad
    obstaculo_2_inicio_y += obstaculo_2_velocidad
    obstaculo_3_inicio_y += obstaculo_3_velocidad
    dragon1_inicio_x += dragon_1_velocidad
    if obstaculo_1_inicio_y >= ALTO_VENTANA:
        obstaculo_1_inicio_y = 100
        obstaculo_1_inicio_x = 200
    if obstaculo_2_inicio_y >= ALTO_VENTANA:
        obstaculo_2_inicio_y = 100
        obstaculo_2_inicio_x = 600
    if obstaculo_3_inicio_y >= ALTO_VENTANA:
        obstaculo_3_inicio_y = 100
        obstaculo_3_inicio_x = 1000
    if dragon1_inicio_x >= ANCHO_VENTANA:
        dragon1_inicio_y = 0
        dragon1_inicio_x = 0
    if colision():
        mostrar_ventana("Perdiste Ingresa cualquier tecla para salir",1)
    pygame.display.update()
    canvas.fill(COLOR_AZUL)
    canvas.blit(fondo1,(0,0))
    obstaculofuncion("imagenes/obstaculo_1.png",obstaculo1_inicio_x,obstaculo_1_inicio_y,obstaculo1_ancho,obstaculo1_alto)
    obstaculofuncion("imagenes/obstaculo_1.png",obstaculo2_inicio_x,obstaculo_2_inicio_y,obstaculo2_ancho,obstaculo2_alto)
    obstaculofuncion("imagenes/obstaculo_1.png",obstaculo3_inicio_x,obstaculo_3_inicio_y,obstaculo3_ancho,obstaculo3_alto)
    persona1funcion(personaje1x,personaje1y)
    obstaculofuncion("imagenes/dragon.png",dragon1_inicio_x,dragon1_inicio_y,dragon1_ancho,dragon1_alto)
    tiempo.tick(50)

pygame.quit()
sys.exit(0)