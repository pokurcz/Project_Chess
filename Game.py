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
                        self.OKNOGRY.blit(image, (x, y))
                    elif self.POLE_GRY[i][j][0] == "B":
                        image = pygame.image.load(
                            "B"+str(self.new_Board.fields[i][j].figura.nazwa)+".png")
                        self.OKNOGRY.blit(image, (x, y))

    def graj(self):  # gra zaprogramowana jako zamienne ruchy z agentem losowym
        pygame.init()
        pygame.display.set_caption('Szachy')
        licznik = 0
        while True:
            self.OKNOGRY.fill((0, 0, 0))
            self.rysuj_plansze()
            self.rysuj_pole_gry()
            pygame.display.update()
            if self.new_Board.player == "B":
                #print(self.new_Board.moves())
                self.new_Board.make_move(random.choice(self.new_Board.moves()))
            else:
                # for x in self.new_Board.moves():
                # print(x[1])
                #wybor = input()
                # self.new_Board.make_move(self.new_Board.moves()[int(wybor)])
                self.new_Board.make_move(random.choice(self.new_Board.moves()))
            time.sleep(2)


new_Game = Game()
new_Game.graj()
