import pygame
import time
import botones
import moviepy.editor


pygame.init()
ventana = pygame.display.set_mode((640, 500))
pygame.display.set_caption("JUEGAZO")


def game():
    import ladrillo

    game_paused = False
    game_win = False

    resume_img = pygame.image.load("imagenes/button_resume.png")
    resume = botones.Button(230, 125, resume_img)

    ball = pygame.image.load("imagenes/ball.png")
    ballrect = ball.get_rect()
    speed = [5, 5]
    ballrect.move_ip(200, 200)

    letra = pygame.image.load("imagenes/letra.png")
    letrarect = letra.get_rect()
    letrarect.move_ip(5, 480)

    bate = pygame.image.load("imagenes/bate.png")
    baterect = bate.get_rect()
    baterect.move_ip(240, 450)

    end = pygame.image.load("imagenes/end.png")
    endrect = end.get_rect()
    endrect.move_ip(0, 0)

    fondo = pygame.image.load("imagenes/fondo.png")
    fondo_rect = fondo.get_rect()

    # Reproduce una cancion que le pasemos
    sonido_fondo = pygame.mixer.Sound("sonidos/sonido_fondo.mp3")
    pygame.mixer.Sound.play(sonido_fondo, 4)

    lista_ladrillos = []
    for posx in range(14):
        for posy in range(3):
            lista_ladrillos.append(ladrillo.Brick(45 * posx, 45 * posy, "imagenes/ladrillo.png"))

    jugando = True  # Bucle principal del juego
    while jugando:
        # Dibujamos los elementos
        ventana.blit(fondo, fondo_rect)
        ventana.blit(ball, ballrect)
        ventana.blit(bate, baterect)

        for ladrillo in lista_ladrillos:
            ventana.blit(ladrillo.image, ladrillo.rect)
            if ballrect.colliderect(ladrillo.rect):
                lista_ladrillos.remove(ladrillo)
                sonido_break = pygame.mixer.Sound("sonidos/sonido_break.mp3")
                pygame.mixer.Sound.play(sonido_break)
                speed[1] = -speed[1]

        if game_paused is True:  # Verifica si el juego está en pausa (P)
            # Dibujamos botones
            if resume.draw(ventana):
                game_paused = False

        else:  # Juego en acción
            ventana.blit(letra, letrarect)
            # Compruebo si hay colisión
            ballrect = ballrect.move(speed)
            if baterect.colliderect(ballrect):
                speed[1] = -speed[1]
            if ballrect.left < 0 or ballrect.right > ventana.get_width():
                speed[0] = -speed[0]
            if ballrect.top < 0:
                speed[1] = -speed[1]
            if ballrect.bottom > ventana.get_height():
                ventana.blit(end, endrect)
                pygame.mixer.stop()
                sonido_gameover = pygame.mixer.Sound("sonidos/gameover.mp3")
                pygame.mixer.Sound.play(sonido_gameover)
                jugando = False

            # Comprueba si se ha pulsado alguna tecla
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and baterect.left > 0:  # Mueve el bate hacia la izquierda
                baterect = baterect.move(-5, 0)
            if keys[pygame.K_RIGHT] and baterect.right < 640:  # Mueve el bate hacia la Derecha
                baterect = baterect.move(5, 0)

        for event in pygame.event.get():  # Comprobamos los eventos
            if event.type == pygame.QUIT:  # Comprobamos si se ha pulsado el botón de cierre de la ventana
                jugando = False
            if event.type == pygame.KEYDOWN:  # Verifica el teclado
                if event.key == pygame.K_p:  # Comprueba si se ha pulsado SPACE
                    game_paused = True  # Cambia el boleano que antes era false
                if event.key == pygame.K_SPACE:
                    game_paused = False

        if len(lista_ladrillos) == 0:  # Comprobamos cuantos ladrillos quedan en el diccionario
            video = moviepy.editor.VideoFileClip("sonidos/yay.mp4")  # Carga el video
            video.preview()  # Reproduce el video
            jugando = False
            game_win = True

        pygame.display.flip()  # Refrescar la pantalla
        pygame.time.Clock().tick(60)  # Controlamos la frecuencia de refresco (FPS)
    return game_win


def gameover(estado):
    if estado is False:
        jugar = True
        while jugar:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    jugar = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        game()
                    if event.key == pygame.K_n:
                        jugar = False
    elif estado is True:
        jugar = True
        while jugar:
            jugar = False


estado_juego = game()
gameover(estado_juego)
time.sleep(0.5)
pygame.quit()
