import pygame
import sys
import random
from board import Board
from board import Field
from pygame.locals import *
import copy
import time


class Game(object):
    def __init__(self):
        self.new_Board = Board()
        self.OKNOGRY = pygame.display.set_mode((400, 400), 0, 32)
        self.POLE_GRY = self.new_Board.plan
        self.obrazki = {}

    def rysuj_plansze(self):  # rysowanie planszy
        for i in range(0, 8):
            for j in range(0, 8):
                if i % 2 == j % 2:
                    pygame.draw.rect(self.OKNOGRY, (155, 155, 155),
                                     Rect(j * 50, i * 50, 50, 50))
                else:
                    pygame.draw.rect(self.OKNOGRY, (35, 35, 35),
                                     Rect(j * 50, i * 50, 50, 50))

    def rysuj_pole_gry(self):  # rysowanie figur
        for i in range(0, 8):
            for j in range(0, 8):
                pole = i * 8 + j
                x = j * 50
                y = i * 50
                if self.new_Board.fields[i][j].figura!=None:
                    if self.POLE_GRY[i][j][0] == "W":
                        image = pygame.image.load(
                            "W"+str(self.new_Board.fields[i][j].figura.nazwa)+".png")
                        self.OKNOGRY.blit(image, (x-5, y-5))
                    elif self.POLE_GRY[i][j][0] == "B":
                        image = pygame.image.load(
                            "B"+str(self.new_Board.fields[i][j].figura.nazwa)+".png")
                        self.OKNOGRY.blit(image, (x-5, y-5))
    def checked_mate(self,board, tmp_move):
        board.make_move(tmp_move)
        if board.player=="W":
            board.player ="B"
        else:
            board.player ="W"
        if board.check()==True:
                return True
        return False

    def graj(self):  # gra zaprogramowana jako zamienne ruchy z agentem losowym
        pygame.init()
        pygame.display.set_caption('Szachy')
        licznik = 0
        while not self.new_Board.draw():
            self.OKNOGRY.fill((0, 0, 0))
            self.rysuj_plansze()
            self.rysuj_pole_gry()
            pygame.display.update()
            Lose = True
            MOVES = self.new_Board.moves()
            for tmp_moves in MOVES:
                if not self.checked_mate(copy.deepcopy(self.new_Board),tmp_moves):
                    Lose = False
                else:
                    MOVES.remove(tmp_moves)
                if 
            if Lose == True:
                print("check_mate")
                break
            self.new_Board.make_move(random.choice(MOVES))
            if self.new_Board.check()==True :
                print("szach milordzie")
            if self.new_Board.player=="W":
                self.new_Board.player ="B"
            else:
                self.new_Board.player ="W"
            self.new_Board.promotion()
            time.sleep(0.5)
            


new_Game = Game()
new_Game.graj()
