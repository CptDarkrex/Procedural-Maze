import random

# Create a 2D array of cells
rows = 12
cols = 24
maze = [['#' for c in range(cols)] for r in range(rows)]

# Choose a random starting cell
start_r = random.randint(0, (rows - 3) // 2) * 2 + 1
start_c = random.randint(0, (cols - 3) // 2) * 2 + 1
maze[start_r][start_c] = '.'

# Create a stack to keep track of visited cells
stack = [(start_r, start_c)]

# Visit all cells in the maze
while stack:
    # Get the current cell
    current_r, current_c = stack[-1]

    # Get a random unvisited neighbor
    neighbors = []
    if current_r > 1 and maze[current_r - 2][current_c] == '#':
        neighbors.append(('N', current_r - 2, current_c))
    if current_r < rows - 2 and maze[current_r + 2][current_c] == '#':
        neighbors.append(('S', current_r + 2, current_c))
    if current_c > 1 and maze[current_r][current_c - 2] == '#':
        neighbors.append(('W', current_r, current_c - 2))
    if current_c < cols - 2 and maze[current_r][current_c + 2] == '#':
        neighbors.append(('E', current_r, current_c + 2))

    if neighbors:
        # Choose a random neighbor and remove the wall
        direction, next_r, next_c = random.choice(neighbors)
        maze[next_r][next_c] = '.'
        maze[current_r + (next_r - current_r) // 2][current_c + (next_c - current_c) // 2] = '.'
        # Push the neighbor onto the stack
        stack.append((next_r, next_c))
    else:
        # Pop the previous cell from the stack
        stack.pop()

# Add barriers on the sides
for r in range(rows):
    maze[r][0] = '|'
    maze[r][-1] = '|'
for c in range(cols):
    maze[0][c] = '_'
    maze[-1][c] = '_'

# Print the maze
for r in range(rows):
    for c in range(cols):
        print(maze[r][c], end='')
    print()

maze = [['#' for c in range(10)] for r in range(10)]
new_maze = []
for row in maze:
    new_maze.append(row)

print(new_maze)



