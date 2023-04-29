import random


class MazeContainer:
    def __init__(self):
        self.player_pos = []
        self.start_x = 0
        self.start_y = 0
        self.exit_obj = "E"  # can be an array or position like above
        self.running = False
        self.moves = {
            "up": [-1, 0],
            "down": [1, 0],
            "left": [0, -1],
            "right": [0, 1],
        }
        self.maze = []

    def generate_maze(self, width, height):
        # Initialize the maze grid
        self.maze = [['#'] * width for _ in range(height)]

        # Starting point
        self.start_x = random.randint(0, width - 1)
        self.start_y = random.randint(0, height - 1)

        exit_x = random.randint(0, width - 1)
        exit_y = random.randint(0, height - 1)

        # Generate the maze
        self.generate_maze_recursive(self.start_x, self.start_y, self.maze)

        # Add entrance and exit points
        self.maze[self.start_y][self.start_x] = 'S'
        self.maze[exit_y][exit_x] = 'E'

        return self.maze

    def init_plr_pos(self):
        self.player_pos = [self.start_y, self.start_x]
        return

    def generate_maze_recursive(self, x, y, maze):
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
                maze[y + dy // 2][x + dx // 2] = '.'
                maze[ny][nx] = '.'

                self.generate_maze_recursive(nx, ny, maze)
        return

    @staticmethod
    def print_maze(inst_maze, inst_player_pos):
        """
        Prints the maze with the player at the given coordinates

        :param inst_maze:
        :param inst_player_pos:
        :return:
        """
        for row_idx, row in enumerate(inst_maze):
            for col_idx, col in enumerate(row):
                if row_idx == inst_player_pos[0] and col_idx == inst_player_pos[1]:
                    print('P', end='')
                else:
                    print(col, end='')
            print()

    def has_won(self, inst_player_pos, inst_exit_pos):
        """
            A function that returns true if player has reached the end point

            :param inst_player_pos:
            :param inst_exit_pos:
            :return bool:
            """
        # return player_pos == inst_exit_pos
        return self.maze[inst_player_pos[0]][inst_player_pos[1]] == inst_exit_pos

    def move_player(self, inst_player_pos, inst_move):
        """
        This function move the player around the maze
        :param inst_player_pos:
        :param inst_move:
        :return:
        """
        new_pos = [inst_player_pos[0] + inst_move[0], inst_player_pos[1] + inst_move[1]]
        if self.maze[new_pos[0]][new_pos[1]] != '#':
            self.player_pos[0], self.player_pos[1] = new_pos[0], new_pos[1]

    def run_game(self):
        if self.running is False:
            self.maze = self.generate_maze(10, 10)
            self.running = True

        self.init_plr_pos()

        while True:
            # Print the maze and ask for the player's move
            self.print_maze(self.maze, self.player_pos)
            move = input('Enter your move (up, down, left, right): ').lower()

            # Move the player and check if they've won
            if move in self.moves:
                self.move_player(self.player_pos, self.moves[move])
                if self.has_won(self.player_pos, self.exit_obj):
                    print('Congratulations! You won!')
                    self.player_pos = [1, 1]
                    break
            else:
                print('Invalid move!')


# maze = MazeContainer()
# maze.run_game()
maze = []
def generate_maze(maze, width, height):
    # Initialize the maze grid
    maze = [['#'] * width for row in range(height)]
    return maze

maze = generate_maze(maze, 10, 10)

for row in maze:
    print(row)
