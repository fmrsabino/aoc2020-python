TREE = '#'
SPACE = '.'


def tree_hit(from_position: (int, int), nav_map: [[str]]) -> int:
    i, j = from_position
    i = (i + 1)

    if i >= len(nav_map):
        return 0

    j = (j + 3) % len(nav_map[i])

    return tree_hit((i, j), nav_map) + (1 if nav_map[i][j] == TREE else 0)


def read_map() -> [[str]]:
    nav_map = []
    with open("map.txt") as file:
        lines = [line.rstrip() for line in file]
        for i, line in enumerate(lines):
            nav_map.append(list())
            for c in line:
                nav_map[i].append(c)
    return nav_map


if __name__ == '__main__':
    nav_map = read_map()
    print(tree_hit((0, 0), nav_map))
