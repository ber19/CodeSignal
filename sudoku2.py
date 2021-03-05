def sudoku2(grid):
    # Inspeccion de filas
    for row in grid:
        diccR = {}
        for i in range(len(row)):
            if row[i] == '.':
                continue
            else:
                if row[i] not in diccR:
                    diccR[row[i]] = 1
                else:
                    diccR[row[i]] += 1
            if diccR[row[i]] > 1:
                return False
    # Inspeccion de columnas
    grid_columns = list(zip(*grid))
    for column in grid_columns:
        diccC = {}
        for i in range(len(column)):
            if column[i] == '.':
                continue
            else:
                if column[i] not in diccC:
                    diccC[column[i]] = 1
                else:
                    diccC[column[i]] += 1
                if diccC[column[i]] > 1:
                    return False
    # Inspeccion de subgrid (3x3)
    for i in range(0,9,3):
        tmpR = 0
        for j in range(0,3):
            subGrid = []
            for k in range(3):
                subGrid += grid[k+i][tmpR:tmpR+3:]
            tmpR += 3
            diccG = {}
            for l in range(0, len(subGrid), 1):
                if subGrid[l] == '.':
                    continue
                else:
                    if subGrid[l] not in diccG:
                        diccG[subGrid[l]] = 1
                    else:
                        diccG[subGrid[l]] += 1
                    if diccG[subGrid[l]] > 1:
                        return False
    return True


gridT = [ ['.', '.', '.', '1', '4', '.', '.', '2', '.'],
          ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
          ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
          ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
          ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
          ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
          ['.', '.', '.', '5', '.', '.', '.', '7', '.'] ]

gridF = [ ['.', '.', '.', '.', '2', '.', '.', '9', '.'],
          ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
          ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
          ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
          ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
          ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
          ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
          ['.', '2', '.', '.', '3', '.', '.', '.', '.'] ]

print(sudoku2(gridT))
