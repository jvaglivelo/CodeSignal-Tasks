def solution(grid):
    #Check rows
    for row in range(len(grid)):
        if rowValid(grid,row) == False:
            return False
        
    #Check columns
    for col in range(len(grid)):
        if colValid(grid,col) == False:
            return False

    #Check subgrids
    for row in range(0,len(grid),3):
        for col in range(0,len(grid),3):
            if subValid(grid,row,col) == False:
                return False
    
    return True
                
def rowValid(grid,row):
    rowArr = []
    for i in range(len(grid)):
        if grid[row][i] in rowArr:
            return False
        elif grid[row][i] != '.':
            rowArr.append(grid[row][i])
    return True

def colValid(grid,col):
    colArr = []
    for i in range(len(grid)):
        if grid[i][col] in colArr:
            return False
        elif grid[i][col] != '.':
            colArr.append(grid[i][col])
    return True

def subValid(grid,sRow,sCol):
    subArr = []
    for row in range(3):
        for col in range(3):
            subValue = grid[sRow + row][sCol + col]
            if subValue in subArr:
                return False
            elif subValue != '.':
                subArr.append(subValue)
    return True
                