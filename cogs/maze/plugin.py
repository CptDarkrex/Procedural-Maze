import random
from modules import Maze_Generator


class MazeContainer:
    def __init__(self):
        self.player_pos = []
        self.start_x = 1
        self.start_y = 1
        self.exit_obj = "E"  # can be a position; Example: [1, 3]
        self.running = False
        self.moves = {
            "up": [-1, 0],
            "down": [1, 0],
            "left": [0, -1],
            "right": [0, 1],
        }
        self.maze_gen = Maze_Generator(maze_size=(40, 40), start_coordinates=(1, 1), end_coordinates=(39, 39))
        self.maze = []
        self.exit_x = random.randint(0, 40 - 1)
        self.exit_y = random.randint(0, 40 - 1)

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
        if self.maze[new_pos[0]][new_pos[1]] != '🌳':
            self.player_pos[0], self.player_pos[1] = new_pos[0], new_pos[1]

    def run_game(self):
        if self.running is False:
            self.maze = self.maze_gen.generate_world(5)

            if self.maze[self.exit_y][self.exit_x] != '🌳':
                self.maze[self.exit_y][self.exit_x] = "E"
            else:
                while self.maze[self.exit_y][self.exit_x] == '🌳':
                    self.exit_y = random.randint(0, 40 - 1)
                    self.exit_x = random.randint(0, 40 - 1)
                self.maze[self.exit_y][self.exit_x] = "E"

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
