class Pieces:  # figury wraz z możliwymi ruchami każdej figury
    def __init__(self, x, y, color):
        self.a = x
        self.b = y
        self.col = color


class Pawn(Pieces):
    nazwa = "P"

    def ruch(self, Plan):
        moz = []
        if(self.col == "W"):
            if(self.a+1 < 9 and Plan[self.a][self.b-1] == "."):
                moz.append(["P", self.a+1, self.b])
            if(self.a == 2 and Plan[self.a][self.b-1] == "." and Plan[self.a+1][self.b-1] == "."):
                moz.append(["P", self.a+2, self.b])
            if self.a+1 < 9 and self.b+1< 9:
                print([Plan[self.a-1][self.b-1],self.a+1, self.b+1] )
            if(self.a+1 < 9 and self.b+1 < 9 and Plan[self.a][self.b][0] == "B"):
                moz.append(["P", self.a+1, self.b+1])
                print("bicie")
            if(self.a+1 < 9 and self.b-1 > 0 and Plan[self.a][self.b-2][0] == "B"):
                moz.append(["P", self.a+1, self.b-1])
                print("bicie")
        else:
            if(self.a-1 > 0 and Plan[self.a-2][self.b-1] == "."):
                moz.append(["P", self.a-1, self.b])
            if(self.a == 7 and Plan[self.a-3][self.b-1] == "." and Plan[self.a-2][self.b-1] == "."):
                moz.append(["P", self.a-2, self.b])
            if(self.a-1 > 0 and self.b-1 > 0 and Plan[self.a-2][self.b-2] != "." and Plan[self.a-2][self.b-2][0] == "W"):
                moz.append(["P", self.a-1, self.b-1])
            if(self.a-1 > 0 and self.b+1 < 9 and Plan[self.a-2][self.b] != "." and Plan[self.a-2][self.b][0] == "W"):
                moz.append(["P", self.a-1, self.b+1])
        return moz

class Bishop(Pieces):
    nazwa = "B"

    def ruch(self, Plan):
        moz = []
        i = self.a+1
        j = self.b+1
        while i <= 8 and j <= 8 and Plan[i-1][j-1] == ".":
            R = ["B", i, j]
            moz.append(R)
            i += 1
            j += 1
        if i-1 <= 8 and j-1 <= 8 and Plan[i-2][j-2][0] != self.col:
            R = ["B", i-1, j-1]
            moz.append(R)
        i = self.a-1
        j = self.b-1
        while i >= 1 and j >= 1 and Plan[i-1][j-1] == ".":
            R = ["B", i, j]
            moz.append(R)
            print(R)
            i -= 1
            j -= 1
        if i+1 >= 1 and j+1 >= 1 and Plan[i][j][0] != self.col:
            R = ["B", i+1, j+1]
            moz.append(R)
        i = self.a+1
        j = self.b-1
        while i <= 8 and j >= 1 and Plan[i-1][j-1] == ".":
            R = ["B", i, j]
            moz.append(R)
            i += 1
            j -= 1
        if i-1 <= 8 and j+1 >= 1 and Plan[i-2][j][0] != self.col:
            R = ["B", i-1, j+1]
            moz.append(R)
        i = self.a-1
        j = self.b+1
        while i >= 1 and j <= 8 and Plan[i-1][j-1] == ".":
            R = ["B", i, j]
            moz.append(R)
            j += 1
            i -= 1
        if i+1 >= 1 and j-1 <= 8 and Plan[i][j-2][0] != self.col:
            R = ["B", i+1, j-1]
            moz.append(R)
        print(moz)
        #return moz


class Queen(Pieces):
    nazwa = "Q"

    def ruch(self, Plan):
        moz = []
        i = self.a+1
        j = self.b+1
        while i <= 8 and j <= 8 and Plan[i-1][j-1] == ".":
            R = ["Q", i, j]
            moz.append(R)
            i += 1
            j += 1
        if i <= 8 and j <= 8 and Plan[i-1][j-1][0] != self.col:
            R = ["Q", i, j]
            moz.append(R)
        i = self.a-1
        j = self.b-1
        while i >= 1 and j >= 1 and Plan[i-1][j-1] == ".":
            R = ["Q", i, j]
            moz.append(R)
            print(R)
            i -= 1
            j -= 1
        if i >= 1 and j >= 1 and Plan[i-1][j-1][0] != self.col:
            R = ["B", i, j]
            moz.append(R)
        i = self.a+1
        j = self.b-1
        while i <= 8 and j >= 1 and Plan[i-1][j-1] == ".":
            R = ["Q", i, j]
            moz.append(R)
            i += 1
            j -= 1
        if i <= 8 and j >= 1 and Plan[i-1][j-1][0] != self.col:
            R = ["Q", i, j]
            moz.append(R)
        i = self.a-1
        j = self.b+1
        while i >= 1 and j <= 8 and Plan[i-1][j-1] == ".":
            R = ["Q", i, j]
            moz.append(R)
            j += 1
            i -= 1
        if i >= 1 and j <= 8 and Plan[i-1][j-1][0] != self.col:
            R = ["Q", i, j]
            moz.append(R)
        i = self.a-1
        while i > 1 and Plan[i-1][self.b-1] == ".":
            R = ["Q", i, self.b]
            moz.append(R)
            i = i-1
        if i > 0 and Plan[i-1][self.b-1][0] != self.col:
            R = ["Q", i, self.b]
            moz.append(R)
        i = self.a+1
        while i < 8 and Plan[i-1][self.b-1] == ".":
            R = ["Q", i, self.b]
            moz.append(R)
            i = i+1
        if i < 9 and Plan[i-1][self.b-1][0] != self.col:
            R = ["Q", i, self.b]
            moz.append(R)

        i = self.b-1
        while i > 1 and Plan[self.a-1][i-1] == ".":
            R = ["Q", self.a, i]
            moz.append(R)
            i = i-1
        if i > 0 and Plan[self.a-1][i-1][0] != self.col:
            R = ["Q", self.a, i]
            moz.append(R)
        i = self.b+1
        while i < 8 and Plan[self.a-1][i-1] == ".":
            R = ["Q", self.a, i]
            moz.append(R)
            i = i+1
        if i < 9 and Plan[self.a-1][i-1][0] != self.col:
            R = ["Q", self.a, i]
            moz.append(R)
        #return moz


class Knight(Pieces):
    nazwa = "K"

    def ruch(self, Plan):
        moz = []
        lista = [1, 2, 3, 4, 5, 6, 7, 8]
        r = []
        r.append([self.a+2, self.b+1])
        r.append([self.a+1, self.b+2])
        r.append([self.a+2, self.b-1])
        r.append([self.a-1, self.b+2])
        r.append([self.a+1, self.b-2])
        r.append([self.a-1, self.b-2])
        r.append([self.a-2, self.b+1])
        r.append([self.a-2, self.b-1])
        for x in r:
            if x[0] in lista and x[1] in lista and Plan[x[0]-1][x[1]-1][0] != self.col:
                moz.append(["K", x[0], x[1]])
        #return moz


class Rook(Pieces):
    nazwa = "R"

    def ruch(self, Plan):
        moz = []
        i = self.a-1
        while i > 1 and Plan[i-1][self.b-1] == ".":
            R = ["R", i, self.b]
            moz.append(R)
            i = i-1
        if i > 0 and Plan[i-1][self.b-1][0] != self.col:
            R = ["R", i, self.b]
            moz.append(R)
        i = self.a+1
        while i < 8 and Plan[i-1][self.b-1] == ".":
            R = ["R", i, self.b]
            moz.append(R)
            i = i+1
        if i < 9 and Plan[i-1][self.b-1][0] != self.col:
            R = ["R", i, self.b]
            moz.append(R)

        i = self.b-1
        while i > 1 and Plan[self.a-1][i-1] == ".":
            R = ["R", self.a, i]
            moz.append(R)
            i = i-1
        if i > 0 and Plan[self.a-1][i-1][0] != self.col:
            R = ["R", self.a, i]
            moz.append(R)
        i = self.b+1
        while i < 8 and Plan[self.a-1][i-1] == ".":
            R = ["R", self.a, i]
            moz.append(R)
            i = i+1
        if i < 9 and Plan[self.a-1][i-1][0] != self.col:
            R = ["R", self.a, i]
            moz.append(R)
        #return moz


class King(Pieces):
    nazwa = "KG"

    def ruch(self, Plan):
        moz = []
        lista = [1, 2, 3, 4, 5, 6, 7, 8]
        r = []
        r.append([self.a+1, self.b+1])
        r.append([self.a+1, self.b-1])
        r.append([self.a+1, self.b])
        r.append([self.a, self.b+1])
        r.append([self.a, self.b-1])
        r.append([self.a-1, self.b+1])
        r.append([self.a-1, self.b-1])
        r.append([self.a-1, self.b])
        for x in r:
            if x[0] in lista and x[1] in lista and Plan[x[0]-1][x[1]-1][0] != self.col:
                moz.append(["KG", x[0], x[1]])
        #return moz
