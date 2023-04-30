import random
from typing import Tuple


maze = [['#' for c in range(10)] for r in range(10)]


def path_generation(point_1: Tuple[int, int], point_2: Tuple[int, int], inst_maze: list):

    distance_y = point_2[0] - point_1[0]
    distance_x = point_2[1] - point_1[1]
    point_stack = [point_1, point_2]

    print(inst_maze[0])

    distance_total = [distance_y, distance_x]

    print(distance_y, distance_x, distance_total)

    for y in enumerate(distance_total):
        print(y[1])

    for i in range(1, distance_total[0] + 1):
        point_stack.append([point_1[0] + i, point_1[1]])

    for i in range(1, distance_total[1]):
        point_stack.append([point_2[0], point_1[1] + i])

    for row_idx, row in enumerate(inst_maze):
        print("row: ", row_idx)
        for col_idx, col in enumerate(row):
            print("column: ", col_idx)
            print([col_idx, row_idx])
            if [col_idx, row_idx] in point_stack:
                print("found index")
                if [col_idx, row_idx] == point_2:
                    inst_maze[col_idx][row_idx] = 'E'
                else:
                    inst_maze[col_idx][row_idx] = '.'

    for row in inst_maze:
        print(row)
    print(point_stack)


path_generation([6, 1], [8, 5], maze)

