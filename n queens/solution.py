def nQueensAll(int):
    if(int < 4):
        raise ValueError("Input must be 4 or greater.")
    valid_solutions = []
    y_cord = 1;
    for i in range(0, int, 1):
        valid_solutions.append((i, y_cord))
        y_cord += 2
        if(y_cord > int-1):
            y_cord = 0
    return valid_solutions

def nQueens(int):
    if(int < 4):
        raise ValueError("Input must be 4 or greater.")
    valid_solutions = []
    y_cord = 1;
    for i in range(0, int, 1):
        valid_solutions.append((i, y_cord))
        y_cord += 2
        if(y_cord > int-1):
            y_cord = 0
    return valid_solutions
