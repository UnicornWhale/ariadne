# -*- coding: utf-8 -*-

from maze_generation import Maze

class Ariadne(object):
    board = None

    def __init__(self):
        self.board = Maze()

    def play(self):
        """
        Begins the main game loop.
        NOTE: Board must be initialized before play is called.
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
