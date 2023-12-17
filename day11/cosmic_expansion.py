import itertools
from typing import List, Tuple

EMPTY = '.'
GALAXY = '#'
UNIVERSE_AGE = 1000000 - 1


def parse_lines(lines: List[str]) -> List[List[str]]:
    return [list(line.strip()) for line in lines]


def get_empty_rows(image: List[List[str]]) -> List[int]:
    return [i for i, row in enumerate(image) if all(element == EMPTY for element in row)]


def find_galaxies(image: List[List[str]]) -> List[Tuple[int, int]]:
    return [(y, x) for y, row in enumerate(image) for x, element in enumerate(row) if element == GALAXY]


def calculate_shortest_paths_sum(galaxies, empty_cols, empty_rows):
    path_sum = 0
    for (y1, x1), (y2, x2) in itertools.combinations(galaxies, 2):
        dy = y2 - y1
        dx = abs(x2 - x1)
        additional_rows = sum(UNIVERSE_AGE for row in empty_rows if y1 < row < y2)
        additional_cols = sum(UNIVERSE_AGE for col in empty_cols if min(x1, x2) < col < max(x1, x2))
        path_sum += dy + dx + additional_rows + additional_cols
    return path_sum


def shortest_paths_sum(image: List[List[str]]) -> int:
    empty_rows = get_empty_rows(image)
    empty_cols = get_empty_rows(list(zip(*image)))
    galaxies = find_galaxies(image)
    return calculate_shortest_paths_sum(galaxies, empty_cols, empty_rows)


def main():
    input_file = '../inputs/input-day-11.txt'
    with open(input_file) as f:
        lines = f.readlines()

    image = parse_lines(lines)
    sum = shortest_paths_sum(image)
    print('Sum of shortest paths: {}'.format(sum))


if __name__ == '__main__':
    main()
