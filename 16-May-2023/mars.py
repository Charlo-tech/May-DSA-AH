def count_adjacent(grid, i, j):
    count = 0
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            ni = i + di
            nj = j + dj
            if 0 <= ni < 5 and 0 <= nj < 5:
                if grid[ni][nj] == 'X':
                    count += 1
            else:
                count += 1
    return count

def update_grid(grid):
    new_grid = [['.' for j in range(5)] for i in range(5)]
    for i in range(5):
        for j in range(5):
            count = count_adjacent(grid, i, j)
            if grid[i][j] == 'X':
                if count == 2 or count == 3:
                    new_grid[i][j] = 'X'
            else:
                if count == 1 or count == 2:
                    new_grid[i][j] = 'X'
    return new_grid

def get_lifeform_score(grid):
    score = 0
    for i in range(5):
        for j in range(5):
            if grid[i][j] == 'X':
                tile = i * 5 + j
                score += 2 ** tile
    return score

grid = [
    ['X', 'X', 'X', 'X', '.'],
    ['X', '.', '.', '.', '.'],
    ['X', '.', '.', 'X', '.'],
    ['.', 'X', '.', 'X', '.'],
    ['X', 'X', '.', 'X', 'X']
]

seen_grids = set()
while True:
    grid_str = ''.join([''.join(row) for row in grid])
    if grid_str in seen_grids:
        lifeform_score = get_lifeform_score(grid)
        print(lifeform_score)
        break
    seen_grids.add(grid_str)
    grid = update_grid(grid)