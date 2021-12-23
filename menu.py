import sys
import pygame


class Menu:  
    def __init__(self, jogo):  # recebe
        self.jogo = jogo
        self.mid_w, self.mid_h = self.jogo.DISPLAY_W / 2, self.jogo.DISPLAY_H / 2  # vai dividir a largura e alt por 22.
        self.run_display = True 
        self.cursor_rect = pygame.Rect(0, 0, 130, 130) # 
        self.offset = - 100

    def desenha_cusor(self): # ▶ vai desenhar o cursor
        self.jogo.desenha_texto('=>', 30, self.cursor_rect.x, self.cursor_rect.y)

    def blit_tela(self):
        self.jogo.window.blit(self.jogo.tela, (0, 0))
        pygame.display.update()
        self.jogo.reseta_teclas()


class MainMenu(Menu):
    def __init__(self, jogo):
        Menu.__init__(self, jogo)
        self.state = "Iniciar"
        self.startx, self.starty = self.mid_w, self.mid_h
        self.tutorialx, self.tutorialy = self.mid_w, self.mid_h + 40
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 80
        self.exitx, self.exity = self.mid_w, self.mid_h + 120
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):  # Aparência do Menu inicial ao jogo
        self.run_display = True
        while self.run_display:
            self.jogo.checar_eventos()
            self.checar_entrada()
            self.jogo.tela.fill(self.jogo.BLACK)  # Preenchendo tela com preto
            self.jogo.desenha_texto('Menu Inicial', 60, self.jogo.DISPLAY_W / 2, self.jogo.DISPLAY_H / 8)
            self.jogo.desenha_texto("Jogar", 30, self.startx, self.starty)
            self.jogo.desenha_texto("Como Jogar?", 30, self.tutorialx, self.tutorialy)
            self.jogo.desenha_texto("Créditos", 30, self.creditsx, self.creditsy)
            self.jogo.desenha_texto("Sair", 30, self.exitx, self.exity)
            self.jogo.desenha_texto("Voltar: Backspace", 20, self.mid_w - 200, self.mid_h + 190)
            self.jogo.desenha_texto("Avancar: Enter", 20, self.mid_w + 200, self.mid_h + 190)
            self.desenha_cusor()
            self.blit_tela()

    def move_cursor(self):  # Movimentação do Cursor (Setinha).
        if self.jogo.DOWN_KEY:  # Usando seta pra baixo
            if self.state == 'Iniciar':
                self.cursor_rect.midtop = (self.tutorialx + self.offset, self.tutorialy)
                self.state = 'Como Jogar?'
            elif self.state == 'Como Jogar?':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Créditos'
            elif self.state == 'Créditos':
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = 'Sair'
            elif self.state == 'Sair':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Iniciar'
        elif self.jogo.UP_KEY:  # Usando ceta pra cima
            if self.state == 'Iniciar':
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = 'Sair'
            elif self.state == 'Sair':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Créditos'
            elif self.state == 'Como Jogar?':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Iniciar'
            elif self.state == 'Créditos':
                self.cursor_rect.midtop = (self.tutorialx + self.offset, self.tutorialy)
                self.state = 'Como Jogar?'

    def checar_entrada(self):
        self.move_cursor()
        if self.jogo.START_KEY:
            if self.state == 'Iniciar':
                self.jogo.playing = True
            elif self.state == 'Como Jogar?':
                self.jogo.curr_menu = self.jogo.opcoes
            elif self.state == 'Créditos':
                self.jogo.curr_menu = self.jogo.creditos
            elif self.state == 'Sair':
                self.jogo.exiting = sys.exit()
            self.run_display = False


class OpcoesMenu(Menu): #Opções do menu que aparecem
    def __init__(self, jogo):
        Menu.__init__(self, jogo)
        self.arrowx, self.arrowy = self.mid_w, self.mid_h + 0
        self.rightx, self.righty = self.mid_w, self.mid_h + 60
        self.leftx, self.lefty = self.mid_w, self.mid_h + 90
        self.shotx, self.shoty = self.mid_w, self.mid_h + 120
        self.shotz, self.shoth = self.mid_w, self.mid_h + 150

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.jogo.checar_eventos()
            self.checar_input()
            self.jogo.tela.fill((0, 0, 0))
            self.jogo.desenha_texto('Tutorial', 40, self.jogo.DISPLAY_W / 2, self.jogo.DISPLAY_H / 2 - 120)
            self.jogo.desenha_texto("Teclado", 30, self.arrowx, self.arrowy)
            self.jogo.desenha_texto("Virar para Direira:  ->", 25, self.rightx, self.righty) #→
            self.jogo.desenha_texto("Virar para Esquerda: <-", 25, self.leftx, self.lefty) #←
            self.jogo.desenha_texto("Pular nível:  TAB", 25, self.shotx, self.shoty)
            self.jogo.desenha_texto("Voltar: Backspace", 15, self.mid_w - 200, self.mid_h + 190)
            self.jogo.desenha_texto("Avançar: Enter", 15, self.mid_w + 200, self.mid_h + 190)
            self.blit_tela()

    def checar_input(self):
        if self.jogo.BACK_KEY:
            self.jogo.curr_menu = self.jogo.main_menu
            self.run_display = False
        elif self.jogo.START_KEY:
            pass


class CreditosMenu(Menu):
    def __init__(self, jogo):
        Menu.__init__(self, jogo)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.jogo.checar_eventos()
            if self.jogo.START_KEY or self.jogo.BACK_KEY:
                self.jogo.curr_menu = self.jogo.main_menu
                self.run_display = False
            self.jogo.tela.fill(self.jogo.BLACK)
            self.jogo.desenha_texto('CRIADORES DE CarRetro', 30, self.jogo.DISPLAY_W / 2, self.jogo.DISPLAY_H / 4 - 20)
            self.jogo.desenha_texto('Robério Ramos', 25, self.jogo.DISPLAY_W / 2, self.jogo.DISPLAY_H / 2 + 10)
            self.jogo.desenha_texto('Italo', 25, self.jogo.DISPLAY_W / 2, self.jogo.DISPLAY_H / 2 + 30)
            self.jogo.desenha_texto('Levi', 25, self.jogo.DISPLAY_W / 2, self.jogo.DISPLAY_H / 2 + 50)
            self.jogo.desenha_texto('OUTRO', 25, self.jogo.DISPLAY_W / 2, self.jogo.DISPLAY_H / 2 + 70)
            self.jogo.desenha_texto('OUTRO', 25, self.jogo.DISPLAY_W / 2, self.jogo.DISPLAY_H / 2 + 90)
            self.jogo.desenha_texto("Voltar: Backspace", 15, self.mid_w - 200, self.mid_h + 190)
            self.jogo.desenha_texto("Avançar: Enter", 15, self.mid_w + 200, self.mid_h + 190)
            self.blit_tela()
