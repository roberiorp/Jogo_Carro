from menu import * # pegando o arquivo Menu / o uso de "*" aparentemente é para incluir tudo
import pygame
import time
import random
from pygame import mixer
class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Laboratio de programação")
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 720, 480 # Tamanho da tela
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = 'fonte/PressStart2P-vaV7.ttf'
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255) #Definindo cores
        self.main_menu = MainMenu(self) #Classes
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu
    def game_loop(self):
            while self.playing:
                self.check_events()
                if self.START_KEY:
                    self.playing = False
# INICIO
                # # #  CONFIGURAÇÕES DE TELA ------------------------------------------------------------------
                pygame.init()
                display_width = 800
                display_height = 600
                black = (0, 0, 0)
                white = (255, 255, 255)
                green = (0, 255, 0)
                red = (255, 0, 0)
                blue = (0, 0, 255)
                car_width = 50
                car_height = 100
                gameDisplay = pygame.display.set_mode((display_width, display_height))
                pygame.display.set_caption("Carro 1.0")
                icon = pygame.image.load('images/icon.png')  # add icon
                pygame.display.set_icon(icon)
                clock = pygame.time.Clock()
                carImg = pygame.image.load("images/kr11.png")  # load the car image
                car2Img = pygame.image.load("images/kr3.png")
                bgImg = pygame.image.load("images/background-5.png")
                crash_img = pygame.image.load("images/crash.png")
                bgsImg = pygame.image.load("images/car.png")
                # # # MUSICA -----------------------------------------------------------------------------------
                mixer.music.load('songs/background.wav')
                mixer.music.play(-1)
                def highscore(count):
                    font = pygame.font.SysFont(None, 45)
                    text = font.render("Score : " + str(count), True, black)
                    gameDisplay.blit(text, (30, 30))
                def draw_things(thingx, thingy, thing):
                    gameDisplay.blit(thing, (thingx, thingy))
                def car(x, y):
                    gameDisplay.blit(carImg, (x, y))
                def text_objects(text, font):
                    textSurface = font.render(text, True, blue)
                    return textSurface, textSurface.get_rect()
                def message_display(text, size, x, y):
                    font = pygame.font.Font("freesansbold.ttf", size)
                    text_surface, text_rectangle = text_objects(text, font)
                    text_rectangle.center = (x, y)
                    gameDisplay.blit(text_surface, text_rectangle)
                def crash(x, y):
                    gameDisplay.blit(crash_img, (x, y))
                    # message_display("You Crashed",64,display_width/2,display_height/2)
                    message_display("GAME OVER", 64, display_width / 2, display_height / 2)
                    pygame.display.update()
                    time.sleep(2)
                    gameloop()
                def gameloop():
                    # pygame.mixer.Sound.stop()
                    pygame.mixer.music.play(-1)
                    bg_x1 = (display_width / 2) - (574 / 2)
                    bg_x2 = (display_width / 2) - (574 / 2)
                    bg_y1 = 0
                    bg_y2 = -600
                    bg_speed = 15
                    bg_speed_change = 0
                    car_x = ((display_width / 2) - (car_width / 2))
                    car_y = (display_height - car_height) - 20
                    car_x_change = 0
                    road_start_x = (display_width / 2) - 151
                    road_end_x = (display_width / 2) + 151
                    thing_startx = random.randrange(road_start_x, road_end_x - car_width)
                    thing_starty = -600
                    thingw = 50
                    thingh = 100
                    thing_speed = 10
                    count = 0
                    gameExit = False
                    while not gameExit:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                gameExit = True
                                pygame.quit()
                                quit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT:
                                    car_x_change = -30
                                elif event.key == pygame.K_RIGHT:
                                    car_x_change = 30
                            if event.type == pygame.KEYUP:
                                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                    car_x_change = 0
                        car_x += car_x_change
                        if car_x > road_end_x - car_width:
                            crash(car_x, car_y)
                        if car_x < road_start_x:
                            crash(car_x - car_width, car_y)
                        if car_y < thing_starty + thingh:
                            if car_x >= thing_startx and car_x <= thing_startx + thingw:
                                crash(car_x - 25, car_y - car_height / 2)
                            if car_x + car_width >= thing_startx and car_x + car_width <= thing_startx + thingw:
                                crash(car_x, car_y - car_height / 2)
                        gameDisplay.fill(green)  # display white background
                        gameDisplay.blit(bgsImg, (0, 0))
                        gameDisplay.blit(bgsImg, (440, 0))
                        gameDisplay.blit(bgImg, (bg_x1, bg_y1))
                        gameDisplay.blit(bgImg, (bg_x2, bg_y2))
                        car(car_x, car_y)  # display car
                        draw_things(thing_startx, thing_starty, car2Img)


                        highscore(count)
                        count += 1  #contador
                        thing_starty += thing_speed  # aqui entra a velocidade dos carros inimigos.

                        if thing_starty > display_height:  # aqui os carros inimigos sumirem e aparecem em uma posição aleatoria.
                            count += 1
                            thing_starty += thing_speed

                        if thing_starty > display_height:
                            thing_startx = random.randrange(road_start_x, road_end_x - car_width)
                            thing_starty = -200

                        bg_y1 += bg_speed
                        bg_y2 += bg_speed

                         # animação da pista para quando a imagem atingir a altura ela volta para a mesma posição.
                        if bg_y1 >= display_height:
                            bg_y1 = -600

                         # animação da pista para quando a imagem atingir a altura ela volta para a mesma posição.
                        if bg_y2 >= display_height:
                            bg_y2 = -600

                        if count > 100:
                            test = 50
                        else:
                            test = 20

                        pygame.display.update()  # atualização da tela

                        clock.tick(test)   # frames por segundo
                        pygame.display.update()  # update the screen
                        clock.tick(test)  # frame por sec

                gameloop()
#FIM
    def check_events(self):
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
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
    def draw_text(self, text, size, x, y ): #Cor da letra, tamanho
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)