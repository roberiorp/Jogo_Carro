from menu import *  # pegando o arquivo Menu / o uso de "*" aparentemente é para incluir tudo
import pygame
import time
import random
from pygame import mixer


class Jogo:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Laboratio de programação")
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 720, 480  # Tamanho da tela
        self.tela = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.font_nome = 'fonte/mieszkanie9.otf'
        self.BLACK, self.WHITE, self.CINZA = (0, 0, 0), (255, 255, 255), (150,150,150) # Definindo cores
        self.main_menu = MainMenu(self)  # Classes
        self.opcoes = OpcoesMenu(self)
        self.creditos = CreditosMenu(self)
        self.curr_menu = self.main_menu

    def loop_jogo(self):
        while self.playing:
            self.checar_eventos()
            if self.START_KEY:
                self.playing = False
            # INICIO
            # # #  CONFIGURAÇÕES DE TELA ------------------------------------------------------------------
            pygame.init()
            tela_width = 800
            tela_height = 600
            black = (0, 0, 0)
            white = (255, 255, 255)
            green = (0, 255, 0)
            red = (255, 0, 0)
            blue = (0, 0, 255)
            carro_width = 50
            carro_height = 100
            telaJogo = pygame.display.set_mode((tela_width, tela_height))
            pygame.display.set_caption("Carro 1.0")
            icone = pygame.image.load('images/icon.png')  # add icon
            pygame.display.set_icon(icone)
            clock = pygame.time.Clock()
            carroImg = pygame.image.load("images/kr11.png")  # load the car image
            carro2Img = pygame.image.load("images/kr3.png")
            bgImg = pygame.image.load("images/background-5.png")
            colisao_img = pygame.image.load("images/crash.png")
            bgsImg = pygame.image.load("images/car.png")
            # # # MUSICA -----------------------------------------------------------------------------------
            mixer.music.load('songs/background.wav')
            #mixer.music.load('songs/loop_0.wav')
            mixer.music.play(-1)

            def highscore(count):
                font = pygame.font.SysFont(None, 45)
                text = font.render("Score : " + str(count), True, black)
                telaJogo.blit(text, (30, 30))

            def desenha_obstalos(thingx, thingy, thing):
                telaJogo.blit(thing, (thingx, thingy))

            def carro(x, y):
                telaJogo.blit(carroImg, (x, y))

            def text_objects(text, font):
                textSurface = font.render(text, True, blue)
                return textSurface, textSurface.get_rect()

            def messagem_tela(text, size, x, y):
                font = pygame.font.Font("freesansbold.ttf", size)
                text_surface, text_rectangle = text_objects(text, font)
                text_rectangle.center = (x, y)
                telaJogo.blit(text_surface, text_rectangle)

            def colisao(x, y):
                telaJogo.blit(colisao_img, (x, y))
                messagem_tela("GAME OVER", 64, tela_width / 2, tela_height / 2)
                pygame.display.update()
                time.sleep(2)
                gameloop()

            def gameloop():
                # pygame.mixer.Sound.stop()
                pygame.mixer.music.play(-1)
                bg_x1 = (tela_width / 2) - (574 / 2)
                bg_x2 = (tela_width / 2) - (574 / 2)
                bg_y1 = 0
                bg_y2 = -600
                bg_velocidade = 15
                bg_velocidade_mudar = 0
                carro_x = ((tela_width / 2) - (carro_width / 2))
                carro_y = (tela_height - carro_height) - 20
                carro_x_mudar = 0
                road_start_x = (tela_width / 2) - 151
                road_end_x = (tela_width / 2) + 151
                carroInimigo_inicioX = random.randrange(road_start_x, road_end_x - carro_width)
                carroInimigo_starty = -600
                carroInimigoW = 50
                carroInimigoH = 100
                carroInimigo_velocidade = 20
                contador = 0
                nivel = 1
                dificuldade = 100
                gameExit = False
                while not gameExit:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            gameExit = True
                            pygame.quit()
                            quit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT:
                                carro_x_mudar = -30
                            elif event.key == pygame.K_RIGHT:
                                carro_x_mudar = 30
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                carro_x_mudar = 0
                        if event.type == pygame.KEYDOWN: # Almenta dificuldade com tecla TAB
                            if event.key == pygame.K_TAB:
                                if bg_velocidade < 40:
                                    bg_velocidade += 5
                                    carroInimigo_velocidade += 5
                                    nivel += 1
                                    niv = 'Nivel '
                                    niv += str(nivel)
                                    messagem_tela(niv, 50, tela_width / 2, tela_height / 2)
                                    pygame.display.update()
                                    time.sleep(0.2)
                    if contador == dificuldade: # Almenta dificuldade automatico
                        if bg_velocidade < 40:
                            bg_velocidade += 5
                            carroInimigo_velocidade += 5
                            dificuldade += 100
                            nivel += 1
                            niv = 'Nivel '
                            niv += str(nivel)
                            messagem_tela(niv, 50, tela_width / 2, tela_height / 2)
                            pygame.display.update()
                            time.sleep(0.2)
                    carro_x += carro_x_mudar
                    if carro_x > road_end_x - carro_width:
                        colisao(carro_x, carro_y)
                    if carro_x < road_start_x:
                        colisao(carro_x - carro_width, carro_y)
                    if carro_y < carroInimigo_starty + carroInimigoH:
                        if carro_x >= carroInimigo_inicioX and carro_x <= carroInimigo_inicioX + carroInimigoW:
                            colisao(carro_x - 25, carro_y - carro_height / 2)
                        if carro_x + carro_width >= carroInimigo_inicioX and carro_x + carro_width <= carroInimigo_inicioX + carroInimigoW:
                            colisao(carro_x, carro_y - carro_height / 2)
                    telaJogo.fill(green)  # display white background
                    telaJogo.blit(bgsImg, (0, 0))
                    telaJogo.blit(bgsImg, (440, 0))
                    telaJogo.blit(bgImg, (bg_x1, bg_y1))
                    telaJogo.blit(bgImg, (bg_x2, bg_y2))
                    carro(carro_x, carro_y)  # display car
                    desenha_obstalos(carroInimigo_inicioX, carroInimigo_starty, carro2Img)

                    highscore(contador)
                    contador += 1  # contador
                    carroInimigo_starty += carroInimigo_velocidade  # aqui entra a velocidade dos carros inimigos.

                    if carroInimigo_starty > tela_height:  # aqui os carros inimigos sumirem e aparecem em uma posição aleatoria.
                        contador += 1
                        carroInimigo_starty += carroInimigo_velocidade

                    if carroInimigo_starty > tela_height:
                        carroInimigo_inicioX = random.randrange(road_start_x, road_end_x - carro_width)
                        carroInimigo_starty = -200

                    bg_y1 += bg_velocidade
                    bg_y2 += bg_velocidade

                    # animação da pista para quando a imagem atingir a altura ela volta para a mesma posição.
                    if bg_y1 >= tela_height:
                        bg_y1 = -600

                    # animação da pista para quando a imagem atingir a altura ela volta para a mesma posição.
                    if bg_y2 >= tela_height:
                        bg_y2 = -600

                    pygame.display.update()  # atualização da tela

                    clock.tick(20)  # frames por segundo

            gameloop()

    # FIM
    def checar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE or event.key == pygame.K_ESCAPE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.UP_KEY = True

    def reseta_teclas(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def desenha_texto(self, texto, tamanho, x, y):  # Cor da letra, tamanho
        fonte = pygame.font.Font(self.font_nome, tamanho)
        texto_surface = fonte.render(texto, True, self.WHITE)
        texto_rect = texto_surface.get_rect()
        texto_rect.center = (x, y)
        self.tela.blit(texto_surface, texto_rect)
