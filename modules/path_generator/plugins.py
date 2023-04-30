import random
from typing import Tuple


class Path_Generator:

    def __init__(self, maze_size: Tuple[int, int], jump_max_size: Tuple[int, int],
                 start_coordinates: Tuple[int, int], finish_coordinates: Tuple[int, int]):
        self.coordinates_stack = []
        self.coordinates_temp_stack = []

        self.maze = []

        self.x_future_coordinate = 0
        self.y_future_coordinate = 0

        self.x_local_distance = 0
        self.y_local_distance = 0

        self.x_distance = finish_coordinates[1] - start_coordinates[1]
        self.y_distance = finish_coordinates[0] - start_coordinates[0]

        self.maze_width = maze_size[1]
        self.maze_height = maze_size[0]

        self.x_jump_max_size = jump_max_size[0]
        self.y_jump_max_size = jump_max_size[1]

        self.x_start = start_coordinates[0]
        self.y_start = start_coordinates[1]

        self.x_finish = finish_coordinates[0]
        self.y_finish = finish_coordinates[1]

        self.x_curr_coordinate = self.x_start
        self.y_curr_coordinate = self.y_start

        self.player_pos = [random.randint(0, self.maze_height - 1), random.randint(0, self.maze_width - 1)]

    def __str__(self):
        return self.coordinates_stack

    def generate_direct_path(self, print_result=False):
        # 1- Determine distance between start / finish in x/y
        # 2- Determine random size jump number to be min between random and distance in x/y
        # 3- Calculate x/y coordinate for next move
        # 4- Append x/y move to move stack
        # 5- Repeat until distance is 0 for x/y

        # Clean move stack, so it doesn't preserve moves from previous calls
        self.coordinates_stack = []
        self.maze = [['#'] * self.maze_width for row in range(self.maze_height)]

        x_step = 0
        y_step = 0

        # Repeat until target is reached in x/y
        while self.x_distance and self.y_distance != 0:
            # 1- Determine (update) distance between current coordinate / finish in x/y
            self._update_xy_distance()

            # 2- Generate a random int between 0 and the minimum between the current x/y distance and the max jump size
            x_step = random.randint(0, min(self.x_distance, self.x_jump_max_size))
            y_step = random.randint(0, min(self.y_distance, self.y_jump_max_size))

            # 3- Calculate x/y coordinate for next move

            self.x_future_coordinate = self.x_curr_coordinate + x_step
            self.y_future_coordinate = self.y_curr_coordinate + y_step

            # 4- Append x/y move to move stack

            self._update_local_distance()

            for i in range(0, self.y_local_distance + 1):
                self.coordinates_temp_stack.append([self.y_curr_coordinate + i, self.x_curr_coordinate])

            self.y_curr_coordinate = self.y_future_coordinate

            for i in range(0, self.x_local_distance + 1):
                self.coordinates_temp_stack.append([self.y_curr_coordinate, self.x_curr_coordinate + i])

            # 5- Repeat until distance is 0 for x/y

            self.coordinates_stack.append([self.y_curr_coordinate, self.x_curr_coordinate])
            self.x_curr_coordinate += x_step
            # self.y_curr_coordinate += y_step

        print(self.coordinates_stack)

        for item in self.coordinates_temp_stack:
            self.coordinates_stack.append(item)

        print(f"temporary coor: {self.coordinates_temp_stack}")
        print(f"full stack: {self.coordinates_stack}")
        self.print_maze()

    def _update_xy_distance(self):
        self.x_distance = self.x_finish - self.x_curr_coordinate
        self.y_distance = self.y_finish - self.y_curr_coordinate

    def _update_local_distance(self):
        self.y_local_distance = self.y_future_coordinate - self.y_curr_coordinate
        self.x_local_distance = self.x_future_coordinate - self.x_curr_coordinate

    def print_maze(self):
        """
        Prints the maze with the player at the given coordinates

        :param inst_maze:
        :param inst_player_pos:
        :return:
        """
        for item in self.coordinates_stack:
            self.maze[item[0]][item[1]] = "."

        for row in self.maze:
            print(row)

# Remove, just for testing
path_maze = Path_Generator([40, 40], [5, 5], [1, 1], [39, 39])
path_maze.generate_direct_path()


