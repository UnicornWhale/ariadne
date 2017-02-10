# -*- coding: utf-8 -*-

from tkinter import *

from maze_generation.maze import Maze
from settings import *

class Ariadne(Canvas):
    board = None

    def __init__(self, master=None):
        Canvas.__init__(self, master, width=MAP_WIDTH*TILE_SIZE, height=MAP_HEIGHT*TILE_SIZE)
        self.master = master
        self.master.title = TITLE
        self.pack(fill=BOTH, expand=1)

        self.board = Maze(self)

    def play(self):
        """
        Begins the main game loop.
        """
        done = False
        while not done:
            move = get_next_move()
            move_player(move)
            if self.board.game_is_over():
                done = True
        return 'Victory!'

    def get_next_move(self):
        """Waits for the player to input a move, then returns the move"""
        return None

    def move_player(self, move):
        """Moves the player in the direction indicated if the move is valid"""
        valid = self.board.is_valid_move(move)
        if valid:
            print('Valid move.')
        else:
            print('Invalid move.')

def main():
    root = Tk()
    canvas = Ariadne(root)
    root.mainloop()

if __name__ == '__main__':
  main()
