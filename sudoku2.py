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
                    return False 

    # Inspeccion de columnas
    inCols = zip(*grid)
    for col in inCols:
        diccC = {}
        for j in range(len(col)):
            if col[j] == '.':
                continue
            else:
                if col[j] not in diccC:
                    diccC[col[j]] = 1
                else:
                    return False

    # Inspeccion de subgrids (3x3)
    for l in range(0, len(grid), 3):
        for i in range(0, len(grid), 3):
            subgrid = {}
            for k in range(3):
                for j in range(l, l+3, 1):
                    if grid[i+k][j] != '.':
                        if grid[i+k][j] not in subgrid:
                            subgrid[grid[i+k][j]] = 1
                        else:
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
