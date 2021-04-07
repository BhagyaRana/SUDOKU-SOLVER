import numpy as np
class solveSudoku:
    r = set()
    c = set()
    s = set()
    def __init__(self,board,row = r,col = c,sub = s):
        self.row = row
        self.col = col
        self.sub = sub
        self.board = board
        pass
   
    def solvesudoku(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] != 0:
                    val = self.board[i][j]
                    rowval = (i*10) + val
                    colval = (j*10) + val
                    subval = (((3*(i/3)*10) + (3*(j/3)))*10 + val)
                    self.row.add(rowval)
                    self.col.add(colval)
                    self.sub.add(subval)
                    pass
        self.solve(0,0)
        pass
    def solve(self,row,col):
        if row == len(self.board):
            return True
        newrow = row
        newcol = col
        if col == len(self.board[0])-1:
            newcol = 0
            newrow += 1
            pass
        else:
            newcol+=1
            pass
        if self.board[row][col] != 0:
            return self.solve(newrow,newcol)
        for i in range(1,10):
            if self.check(row,col,i):
                self.board[row][col] = i
                if self.solve(newrow,newcol):
                    return True
                self.removerc(row,col,i)
                self.board[row][col] = 0
        return False
    def removerc(self,i,j,val):
        rowVal=(i*10)+val
        colVal=(j*10)+val
        subRow=(30*(i/3))
        subCol=(3*(j/3))
        subVal= (subRow+subCol)*10+val
        self.row.remove(rowVal)
        self.col.remove(colVal)
        self.sub.remove(subVal)
        pass

    def check(self,i,j,val):
        rowVal=(i*10)+val
        colVal=(j*10)+val
        subRow=(30*(i/3))
        subCol=(3*(j/3))
        subVal= (subRow+subCol)*10+val
        if (rowVal in self.row)or(colVal in self.col)or(subVal in self.sub):
            return False
        self.row.add(rowVal)
        self.col.add(colVal)
        self.sub.add(subVal)
        return True
    pass

grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

print("The original matrix: ")
print(np.matrix(grid))
sol = solveSudoku(grid)
print("The solved matrix: ")
sol.solvesudoku()
print(np.matrix(grid))

        
