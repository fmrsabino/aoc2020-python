import re

BAGS = {}

KEY_VALUE_PATTERN = re.compile("(.+) bags contain (.+)")
CONTENTS_PATTERN = re.compile("([0-9]+) (.+) bags?")


def parse_bag_contents(raw_contents: str) -> []:
    contents = set()
    for content in raw_contents.split(","):
        for match in CONTENTS_PATTERN.finditer(content.strip()):
            contents.add(match.group(2))
    return contents


def read_input():
    for line in open("input.txt"):
        for match in KEY_VALUE_PATTERN.finditer(line):
            BAGS[match.group(1)] = parse_bag_contents(match.group(2))


def search_bags(target_bags: set) -> {}:
    container_bags = {bag for target_bag in target_bags for (bag, contents) in BAGS.items() if target_bag in contents}
    if len(container_bags) == 0:
        return container_bags
    else:
        return container_bags.union(search_bags(container_bags))


if __name__ == '__main__':
    read_input()
    result = len(search_bags({'shiny gold'}))
    print(f'{result} bags')
