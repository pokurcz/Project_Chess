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

    def drawing_Board(self):
        for i in range(0, 8):
            for j in range(0, 8):
                if i % 2 == j % 2:
                    pygame.draw.rect(self.OKNOGRY, (155, 155, 155),
                                     Rect(j * 50, i * 50, 50, 50))
                else:
                    pygame.draw.rect(self.OKNOGRY, (35, 35, 35),
                                     Rect(j * 50, i * 50, 50, 50))

    def drawing_pieces(self):
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

    def graj(self):  # game beetween random agents
        pygame.init()
        pygame.display.set_caption('Chess')
        licznik = 0
        while True:
            self.OKNOGRY.fill((0, 0, 0))
            self.drawing_Board()
            self.drawing_pieces()
            pygame.display.update()
            MOVES = self.new_Board.moves()
            MOVES_2=[]
            if self.new_Board.checked()==True :
                print("Check")
            for X in MOVES:
                tmp = copy.deepcopy(self.new_Board)
                tmp.make_move(X)
                if  not tmp.checked():
                    MOVES_2.append(X)
            if self.new_Board.checked() and len(MOVES_2)==0:
                if self.new_Board.player=="W":
                    print("Black Win")
                    return None
                else:
                    print("White Win")
                    return None
            if len(MOVES)==0:
                print("Draw")
                return None
            self.new_Board.make_move(random.choice(MOVES_2))
            if self.new_Board.player=="W":
                self.new_Board.player ="B"
            else:
                self.new_Board.player ="W"
            self.new_Board.promotion()
            time.sleep(0.1)
            


new_Game = Game()
new_Game.graj()
