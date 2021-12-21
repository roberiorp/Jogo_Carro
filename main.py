from jogo import Game  # Pegando o arquivo game e importando a classe Game

g = Game()  # facilitar toda a bagaça!

while 1:
    g.curr_menu.display_menu()  # função menu
    g.game_loop()

pygame.quit()