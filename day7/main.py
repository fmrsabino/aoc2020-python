import re

BAGS = {}

KEY_VALUE_PATTERN = re.compile("(.+) bags contain (.+)")
CONTENTS_PATTERN = re.compile("([0-9]+) (.+) bags?")


def parse_bag_contents(raw_contents: str) -> {}:
    return {
        (int(match.group(1)), match.group(2))
        for content in raw_contents.split(",")
        for match in CONTENTS_PATTERN.finditer(content.strip())
    }


def read_input():
    for line in open("input.txt"):
        for match in KEY_VALUE_PATTERN.finditer(line):
            BAGS[match.group(1)] = parse_bag_contents(match.group(2))


def search_bags(target_bags: set) -> {}:
    container_bags = {
        bag for (bag, contents) in BAGS.items()
        for target_bag in target_bags
        if target_bag in {c for (_, c) in contents}
    }

    return container_bags if len(container_bags) == 0 else container_bags.union(search_bags(container_bags))


def part2(target: str) -> int:
    return sum(n + n * part2(bag)
               for (n, bag) in BAGS[target])


if __name__ == '__main__':
    read_input()
    print(f'Part 1: {len(search_bags({"shiny gold"}))} bags')
    print(f'Part 2: {part2("shiny gold")}')
