import random


class MazeContainer:
    def __init__(self):
        self.player_pos = []

        self.maze_width = 24
        self.maze_height = 12

        self.start_x = 0
        self.start_y = 0

        self.exit_obj = "E"  # can be a position; Example: [1, 3]

        self.running = False

        self.maze = []

        self.stack = ''
        self.moves = {
            "up": [-1, 0],
            "down": [1, 0],
            "left": [0, -1],
            "right": [0, 1],
        }

    def generate_maze(self, width, height):
        # Initialize the maze grid
        #self.maze = [['#'] * width for row in range(height)]
        self.maze = [['#' for c in range(height)] for r in range(width)]
        print(self.maze)

        # Starting point
        self.start_x = random.randint(0, (width - 3) // 2) * 2 + 1
        self.start_y = random.randint(0, (height - 3) // 2) * 2 + 1

        exit_x = random.randint(0, (width - 3) // 2) * 2 + 1
        exit_y = random.randint(0, (height - 3) // 2) * 2 + 1

        # Generate the maze
        self.maze[self.start_y][self.start_x] = '.'
        # Create a stack to keep track of visited cells
        self.stack = [(self.start_y, self.start_x)]

        # Visit all cells in the maze
        while self.stack:
            # Get the current cell
            current_r, current_c = self.stack[-1]

            # Get a random unvisited neighbor
            neighbors = []
            if current_r > 1 and self.maze[current_r - 2][current_c] == '#':
                neighbors.append(('N', current_r - 2, current_c))
            if current_r < height - 2 and self.maze[current_r + 2][current_c] == '#':
                neighbors.append(('S', current_r + 2, current_c))
            if current_c > 1 and self.maze[current_r][current_c - 2] == '#':
                neighbors.append(('W', current_r, current_c - 2))
            if current_c < width - 2 and self.maze[current_r][current_c + 2] == '#':
                neighbors.append(('E', current_r, current_c + 2))

            if neighbors:
                # Choose a random neighbor and remove the wall
                direction, next_r, next_c = random.choice(neighbors)
                self.maze[next_r][next_c] = '.'
                self.maze[current_r + (next_r - current_r) // 2][current_c + (next_c - current_c) // 2] = '.'
                # Push the neighbor onto the stack
                self.stack.append((next_r, next_c))
            else:
                # Pop the previous cell from the stack
                self.stack.pop()

        # Add barriers on the sides
        for r in range(height):
            self.maze[r][0] = '|'
            self.maze[r][-1] = '|'
        for c in range(width):
            self.maze[0][c] = '_'
            self.maze[-1][c] = '_'

        # Print the maze
        for r in range(height):
            for c in range(width):
                print(self.maze[r][c], end='')
            print()

        # Add entrance and exit points
        self.maze[self.start_y][self.start_x] = 'S'
        self.maze[exit_y][exit_x] = 'E'

        return self.maze

    def init_plr_pos(self):
        self.player_pos = [self.start_y, self.start_x]
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
            self.maze = self.generate_maze(self.maze_height, self.maze_width)
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
                    self.running = False
                    break
            else:
                print('Invalid move!')


maze = MazeContainer()
maze.generate_maze(24, 24)
