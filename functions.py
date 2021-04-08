N = 9

def isPossible(grid, row, col, num):
	for x in range(9):
		if grid[row][x] == num:
			return False
	for x in range(9):
		if grid[x][col] == num:
			return False
	startRow = row - row % 3
	startCol = col - col % 3
	for i in range(3):
		for j in range(3):
			if grid[i + startRow][j + startCol] == num:
				return False
	return True

def solve1(grid, row, col):
	if (row == N - 1 and col == N):
		return True
	if col == N:
		row += 1
		col = 0
	if grid[row][col] > 0:
		return solve1(grid, row, col + 1)
	for num in range(1, N + 1, 1):
		if isPossible(grid, row, col, num):
			grid[row][col] = num
			if solve1(grid, row, col + 1):
				return True
		grid[row][col] = 0
	return False

row=set()
col=set()
sub=set()

def solve2 (board):
    row.clear()
    col.clear()
    sub.clear()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j]!=0):
                val = board[i][j]
                rowval = (i*10)+(val)
                colval = (j*10)+(val)
                subval = (((3*(i/3)*10)+(3*(j/3)))*10 +val)

                row.add(rowval)
                col.add(colval)
                sub.add(subval)
    solve(board,0,0)

def solve(board,row,col):
    if(row==len(board)):
        return True             

    newrow=row
    newcol=col
    if(col==len(board[0])-1):
        newcol=0
        newrow+=1
    else:
        newcol+=1
    
    if(board[row][col]!=0):
        return solve(board,newrow,newcol)
    
    for i in range(1,10):
        if(check(row,col,i)):
            board[row][col]=i
            if(solve(board,newrow,newcol)):
                return True
            
            remove(row,col,i)
            board[row][col]=0
    return False

def remove(i,j,val):
    rowVal=(i*10)+val
    colVal=(j*10)+val
    subRow=(30*(i/3))
    subCol=(3*(j/3))
    subVal= (subRow+subCol)*10+val
            
    row.remove(rowVal)
    col.remove(colVal)
    sub.remove(subVal)

def check(i,j,val):
    rowVal=(i*10)+val
    colVal=(j*10)+val
    subRow=(30*(i/3))
    subCol=(3*(j/3))
    subVal= (subRow+subCol)*10+val

    if( (rowVal in row) or (colVal in col) or (subVal in sub) ):          
    # if(row.contains(rowVal) or col.contains(colVal) or sub.contains(subVal) ):
        return False
    
    row.add(rowVal)
    col.add(colVal)
    sub.add(subVal)
    return True