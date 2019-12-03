from typing import List, Set, Tuple

def read_paths(filename: str) -> List[List]:
    with open(filename,'r') as f:
        paths = f.readlines()

    return [path.strip().split(',') for path in paths]


def translate_instruction_to_grid(grid: Set,
                                  start: List,
                                  instr: str) -> List:

    direct = instr[0]
    value = int(instr[1:])

    if direct == 'R':
        grid = expand_to_points([start[0],start[0]+value],
                                [start[1],start[1]],grid)
        start = [start[0]+value,start[1]]
    elif direct == 'L':
        grid = expand_to_points([start[0]-value,start[0]],
                                [start[1],start[1]],grid)
        start = [start[0]-value,start[1]]
    elif direct == 'U':
        grid = expand_to_points([start[0],start[0]],
                                [start[1],start[1]+value],grid)
        start = [start[0],start[1]+value]
    elif direct == 'D':
        grid = expand_to_points([start[0],start[0]],
                                [start[1]-value,start[1]],grid)
        start = [start[0],start[1]-value]
    else:
        raise ValueError(f'Invalid direction {direct}')

    return grid,start


def expand_to_points(xs: List, ys: List, grid: Set) -> Set:

    for x in range(xs[0],xs[1]+1):
        for y in range(ys[0],ys[1]+1):
            grid.add((x,y))

    return grid


def manhattan_distance(p1: List, p2: List):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])


def closest_intersection_dist(instructs1: List,
                              instructs2: List) -> List:

    grid1 = set()
    grid2 = set()
    start1,start2 = [0,0],[0,0]
    for instruct in instructs1:
        grid1,start1 = translate_instruction_to_grid(grid1,start1,instruct)

    for instruct in instructs2:
        grid2,start2 = translate_instruction_to_grid(grid2,start2,instruct)

    intersections = grid1.intersection(grid2)
    intersections.remove((0,0))

    dists = [manhattan_distance([0,0],intersection)\
             for intersection in intersections]

    return intersections, min(dists)


def move(position: List, instruct: str) -> List:

    direct = instruct[0]
    value = int(instruct[1:])

    if direct == 'R':
        position[0] += value
    elif direct == 'L':
        position[0] -= value
    elif direct == 'U':
        position[1] += value
    elif direct == 'D':
        position[1] -= value
    else:
        raise ValueError(f'Invalid direction {direct}')

    return position, value

def is_between(pos1: List, pos2: List, target: List) -> bool:

    if pos1[0] < pos2[0]:
        x_between = pos1[0] <= target[0] <= pos2[0]
    else:
        x_between = pos2[0] <= target[0] <= pos1[0]

    if pos1[1] < pos2[1]:
        y_between = pos1[1] <= target[1] <= pos2[1]
    else:
        y_between = pos2[1] <= target[1] <= pos1[1]

    return x_between and y_between

def path_length_to_intersection(instructs: List, intersection: Tuple) -> int:

    path_length = 0
    old_position = [0, 0]
    intersection = list(intersection)

    for instr in instructs:
        position, length = move(old_position.copy(),instr)

        if is_between(old_position,position,intersection):
            path_length += manhattan_distance(old_position,intersection)
            break
        else:
            path_length += length
            old_position = position.copy()

    return path_length


def shortest_path_to_intersection(instructs1: List,
                                  instructs2: List) -> int:

    intersections, _ = closest_intersection_dist(instructs1, instructs2)

    path_lengths = []
    for intersc in intersections:
        length1 = path_length_to_intersection(instructs1,intersc)
        length2 = path_length_to_intersection(instructs2,intersc)
        path_lengths.append(length1 + length2)

    return min(path_lengths)


def tests() -> None:

    assert(closest_intersection_dist(['R8','U5','L5','D3'],
                                     ['U7','R6','D4','L4'])[1] == 6)
    assert(closest_intersection_dist(
        ['R75','D30','R83','U83','L12','D49','R71','U7','L72'],
        ['U62','R66','U55','R34','D71','R55','D58','R83'])[1] == 159)
    assert(closest_intersection_dist(
        ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],
        ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7'])[1] == 135)

    assert(shortest_path_to_intersection(
            ['R75','D30','R83','U83','L12','D49','R71','U7','L72'],
            ['U62','R66','U55','R34','D71','R55','D58','R83']) == 610)

    assert(shortest_path_to_intersection(
        ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],
        ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']) == 410)


def main():

    tests()

    paths = read_paths('day3.dat')
    _, dist = closest_intersection_dist(paths[0],paths[1])
    print(f'closest intersection is {dist} units away.')

    steps = shortest_path_to_intersection(paths[0],paths[1])
    print(f'shortest path to an intersection takes {steps} steps.')


if __name__ == '__main__':
    main()
