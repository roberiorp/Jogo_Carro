from jogo import Jogo  # Pegando o arquivo game e importando a classe Game

g = Jogo()  # para facilitar!

while 1:
    g.curr_menu.display_menu()  # função para o menu!
    g.loop_jogo()               # Loop para ficar rodando jogo!

pygame.quit()