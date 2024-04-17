# main.py
from game import Game
from menu import Menu

if __name__ == "__main__":
    game = Game()
    menu = Menu(game.screen)
    game.run()
