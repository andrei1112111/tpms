from random import uniform
import matplotlib.pyplot as plt


def grid():
    maze = [[is_empty_cell(prob / 1000) for cell in range(width)] for line in range(height)]
    ''' Maze Properties'''
    num_rows = len(maze)
    num_cols = len(maze[0])
    end_pt = (num_cols - 1, num_rows - 1)
    start_pt = (0, 0)

    '''BFS'''
    visited = {end_pt: None}
    queue = [end_pt]
    while queue:
        current = queue.pop(0)
        if current == start_pt:
            shortest_path = []
            while current:
                shortest_path.append(current)
                current = visited[current]
            return 1
        adj_points = []
        '''FIND ADJACENT POINTS'''
        current_col, current_row = current
        #UP
        if current_row > 0:
            if maze[current_row - 1][current_col] == 0:
                adj_points.append((current_col, current_row - 1))
        #RIGHT
        if current_col < (len(maze[0])-1):
            if maze[current_row][current_col + 1] == 0: ## There was an error here!
                adj_points.append((current_col + 1, current_row))
        #DOWN
        if current_row < (len(maze) - 1):
            if maze[current_row + 1][current_col] == 0:
                adj_points.append((current_col, current_row + 1))
        #LEFT
        if current_col > 0:
            if maze[current_row][current_col - 1] == 0:
                adj_points.append((current_col - 1, current_row))

        '''LOOP THROUGH ADJACENT PTS'''
        for point in adj_points:
            if point not in visited:
                visited[point] = current
                queue.append(point)

    return 0


def is_empty_cell(prob):
    if uniform(0, 1) < prob:
        return 1  # wall
    return 0


width = 12
height = 12

probs = []
solved = []


for prob in range(1001):

    slvd = 0
    for i in range(100):
        slvd += grid()

    probs.append(prob / 1000)
    solved.append(slvd / 100)


plt.scatter(probs, solved, s=1)
plt.xlabel("Вероятность стены")
plt.ylabel("Вероятность что лабиринт можно пройти")
plt.show()
