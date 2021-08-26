from Pieces import Queen
from Pieces import King
from Pieces import Pawn
from Pieces import Bishop
from Pieces import Rook
from Pieces import Knight
import copy
import random


class Field(object):  # pojedyncze pole, wraz z metoda czy jest atakowane
    def __init__(self, x, y, piece):
        self.a = x
        self.b = y
        self.figura = piece

    def be_attacked(self, Board_tmp):
        for i in Board_tmp.moves():
            if i[1][0] == self.a and i[1][1] == self.b:
                return True
            else:
                return False


class Board(object):  # szachownica wraz z ogólną obsługą rozgrywki
    def __init__(self):
        self.plan = [["WR", "WK", "WB", "WQ", "WKG", "WB", "WK", "WR"], ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"], [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."], [
            ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."], ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"], ["BR", "BK", "BB", "BQ", "BKG", "BB", "BK", "BR"]]
        self.player = "W"

        P1 = Pawn(2, 1, "W")
        P2 = Pawn(2, 2, "W")
        P3 = Pawn(2, 3, "W")
        P4 = Pawn(2, 4, "W")
        P5 = Pawn(2, 5, "W")
        P6 = Pawn(2, 6, "W")
        P7 = Pawn(2, 7, "W")
        P8 = Pawn(2, 8, "W")
        K1 = Knight(1, 2, "W")
        K2 = Knight(1, 7, "W")
        R1 = Rook(1, 1, "W")
        R2 = Rook(1, 8, "W")
        B1 = Bishop(1, 3, "W")
        B2 = Bishop(1, 6, "W")
        Q1 = Queen(1, 4, "W")
        KG1 = King(1, 5, "W")
        White_Figure = [R1, K1, B1, Q1, KG1, B2,
                        K2, R2, P1, P2, P3, P4, P5, P6, P7, P8]

        P9 = Pawn(7, 1, "B")
        P10 = Pawn(7, 2, "B")
        P11 = Pawn(7, 3, "B")
        P12 = Pawn(7, 4, "B")
        P13 = Pawn(7, 5, "B")
        P14 = Pawn(7, 6, "B")
        P15 = Pawn(7, 7, "B")
        P16 = Pawn(7, 8, "B")
        K3 = Knight(8, 2, "B")
        K4 = Knight(8, 7, "B")
        R3 = Rook(8, 1, "B")
        R4 = Rook(8, 8, "B")
        B3 = Bishop(8, 3, "B")
        B4 = Bishop(8, 6, "B")
        Q2 = Queen(8, 4, "B")
        KG2 = King(8, 5, "B")
        Black_Figure = [P9, P10, P11, P12, P13, P14,
                        P15, P16, R3, K3, B3, Q2, KG2, B4, K4, R4]

        figure = White_Figure + Black_Figure
        self.fields = [[], [], [], [], [], [], [], []]
        licznik = 0
        for i in range(0, 8):
            for j in range(0, 8):
                if self.plan[i][j] != ".":
                    self.fields[i].append(Field(i, j, figure[licznik]))
                    licznik += 1
                else:
                    self.fields[i].append(Field(i, j, None))
        self.history = []

    def check(self):  # czy jest szach
        for j in self.fields:
            for i in j:
                if i.be_attacked(self) and type(i.figura) == King and (i.figura.col != self.player):
                    return True
                else:
                    return False

    def mate(self):  # czy jest mat
        for field in self.fields:
            for i in field:
                if i.be_attacked(self) and type(i.figura) == King and (i.figura.col == self.player) and len(self.moves()) == 0:
                    return True
                else:
                    return False

    def draw(self):  # czy jest remis
        if len(self.moves()) == 0:
            return True
        licz = 0
        for x in self.history:
            if self.plan == x:
                licz += 1
            if licz > 2:
                return True
        return False

    def moves(self):  # produkowanie możliwych ruchów
        move = []
        for i in self.fields:
            for field in i:
                if field.figura != None and field.figura.col == self.player:
                    move_tmp = field.figura.ruch(self.plan)
                    if move_tmp != None:
                        for m in move_tmp:
                            move.append([field.figura, m])
        return move

    def make_move(self, move_to_do):  # wykonywanie wybranego ruchu
        x_1 = (move_to_do[0].a)-1
        y_1 = (move_to_do[0].b)-1
        x_2 = (move_to_do[1][1])-1
        y_2 = (move_to_do[1][2])-1
        self.plan[x_1][y_1] = "."
        tmp = copy.deepcopy(self.fields[x_1][y_1].figura)
        if(self.fields[x_1][y_1].figura != None):
            print("error")
        if type(tmp) == Pawn:
            self.plan[x_2][y_2] = tmp.col+"P"
        if type(tmp) == Bishop:
            self.plan[x_2][y_2] = tmp.col+"B"
        if type(tmp) == Knight:
            self.plan[x_2][y_2] = tmp.col+"K"
        if type(tmp) == King:
            self.plan[x_2][y_2] = tmp.col+"KG"
        if type(tmp) == Rook:
            self.plan[x_2][y_2] = tmp.col+"R"
        if type(tmp) == Queen:
            self.plan[x_2][y_2] = tmp.col+"Q"
        self.fields[x_2][y_2].a = x_2
        self.fields[x_2][y_2].b = y_2
        self.fields[x_2][y_2].figura = tmp
        self.fields[x_1][y_1] = Field(x_1, y_1, None)
        if self.player == "W":
            self.player = "B"
        else:
            self.player = "W"
        plan = []
        for i in self.plan:
            plan.append(i.copy())
        self.history.append(plan)
        #print(self.history[len(self.history)-1])
