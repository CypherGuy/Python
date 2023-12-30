# DFS approach:
from queue import Queue


def dfs(grid, i, j, old_color, new_color):
    n = len(grid)
    m = len(grid[0])
    if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != old_color:
        return
    else:
        grid[i][j] = new_color
        dfs(grid, i+1, j, old_color, new_color)
        dfs(grid, i-1, j, old_color, new_color)
        dfs(grid, i, j+1, old_color, new_color)
        dfs(grid, i, j-1, old_color, new_color)


def flood_fill_DFS(grid, i, j, new_color):
    old_color = grid[i][j]
    if old_color == new_color:
        return
    dfs(grid, i, j, old_color, new_color)


# BFS approach:


def flood_fill_BFS(grid, i, j, new_color):
    n = len(grid)
    m = len(grid[0])
    old_color = grid[i][j]
    if old_color == new_color:
        return
    queue = Queue()
    queue.put((i, j))
    while not queue.empty():
        i, j = queue.get()
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != old_color:
            continue
        else:
            grid[i][j] = new_color
            queue.put((i+1, j))
            queue.put((i-1, j))
            queue.put((i, j+1))
            queue.put((i, j-1))
