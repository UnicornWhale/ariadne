# -*- coding: utf-8 -*-

from tkinter import *

from settings import *

class Maze(object):
    board = [[None for y in range(MAP_HEIGHT)] for x in range(MAP_WIDTH)]

    def __init__(self, canvas):
        self.canvas = canvas
        self.init_maze()

    def init_maze(self):
        """Initialize self.board to hold a maze"""
        for x in range(MAP_WIDTH):
            for y in range(MAP_HEIGHT):
                self.board[x][y] = self.canvas.create_rectangle(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE, fill='white')

    def is_valid_move(self, move):
        """Returns True if the player can make the desired move, False otherwise"""
        return False

    def game_is_over(self):
        """Returns True if the player has reached the exit, False otherwise"""
        return False
