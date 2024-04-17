# main.py
from game import Game
from menu import Menu
from bottom_interface import BottomInterface

if __name__ == "__main__":
    game = Game()
    bottom_interface = BottomInterface(game.screen)
    menu = Menu(game.screen)
    game.run()
