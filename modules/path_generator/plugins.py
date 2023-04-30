import random
from typing import Tuple


class Path_Generator:

    def __init__(self, maze_size: Tuple[int, int], jump_max_size: Tuple[int, int],
                 start_coordinates: Tuple[int, int], finish_coordinates: Tuple[int, int]):

        self.coordinates_stack = []

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

    def __str__(self):
        return self.coordinates_stack
    def generate_direct_path(self):
        # 1- Determine distance between start / finish in x/y
        # 2- Determine random size jump number to be min between random and distance in x/y
        # 3- Calculate x/y coordinate for next move
        # 4- Append x/y move to move stack
        # 5- Repeat until distance is 0 for x/y

        # Clean move stack, so it doesn't preserve moves from previous calls
        self.coordinates_stack = []

        x_step = 0
        y_step = 0

        x_future_coordinate = 0
        y_future_coordinate = 0

        # Repeat until target is reached in x/y
        while self.x_distance and self.y_distance != 0:
            # 1- Determine (update) distance between current coordinate / finish in x/y
            self._update_xy_distance()

            # 2- Generate a random int between 0 and the minimum between the current x/y distance and the max jump size
            x_step = random.randint(0,min(self.x_distance, self.x_jump_max_size))
            y_step = random.randint(0, min(self.y_distance, self.y_jump_max_size))

            # 3- Calculate x/y coordinate for next move

            self.x_curr_coordinate += x_step
            self.y_curr_coordinate += y_step

            # 4- Append x/y move to move stack
            self.coordinates_stack.append([self.x_curr_coordinate, self.y_curr_coordinate])

            # 5- Repeat until distance is 0 for x/y

    def _update_xy_distance(self):
        self.x_distance = self.x_finish - self.x_curr_coordinate
        self.y_distance = self.y_finish - self.y_curr_coordinate

    #TODO: Define method for filling the coordinate gaps between move steps, insert between after step 4

    #TODO: Define method for printing a nice looking representation of the path

# Remove, just for testing
path_maze = Path_Generator([20,20],[5,5],[1,1],[19,19])
path_maze.generate_direct_path()
print(path_maze.coordinates_stack)