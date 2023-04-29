import random

def generate_maze(width, height):
    # Initialize the maze grid
    maze = [['#'] * width for _ in range(height)]

    # Starting point
    start_x = random.randint(0, width - 1)
    start_y = random.randint(0, height - 1)

    exit_x = random.randint(0, width - 1)
    exit_y = random.randint(0, height - 1)

    # Generate the maze
    generate_maze_recursive(start_x, start_y, maze)

    # Add entrance and exit points
    maze[start_y][start_x] = 'S'
    maze[exit_x][exit_y] = 'E'

    return maze

def generate_maze_recursive(x, y, maze):
    width = len(maze[0])
    height = len(maze)

    # Directions: 0 = up, 1 = right, 2 = down, 3 = left
    directions = [(0, -2), (2, 0), (0, 2), (-2, 0)]
    random.shuffle(directions)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if nx < 0 or ny < 0 or nx >= width or ny >= height:
            continue

        if maze[ny][nx] == '#':
            maze[y + dy // 2][x + dx // 2] = ' '
            maze[ny][nx] = ' '

            generate_maze_recursive(nx, ny, maze)

# Example usage
maze = generate_maze(21, 21)

# Print the maze
for row in maze:
    print(' '.join(row))
