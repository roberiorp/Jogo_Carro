from jogo import Jogo  # Pegando o arquivo game e importando a classe Game

g = Jogo()  # facilitar!

while 1:
    g.curr_menu.display_menu()  # função menu
    g.loop_jogo()               # Loop do jogo

pygame.quit()