import re

policyFormat = re.compile('([0-9]+)-([0-9+]) ([a-z]): (.*)')


def is_password_valid(min_occurrences: int, max_occurrences: int, letter: str, password: str) -> bool:
    return password.count(letter) in range(min_occurrences, max_occurrences + 1)


if __name__ == '__main__':
    lines: [str]
    with open("input.txt") as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip("\n")
        match = policyFormat.match(line)
        if len(match.groups()) != 4:
            raise Exception("Format needs to be 'min-max letter: password'")

        isValid = is_password_valid(
            min_occurrences=int(match.group(1)),
            max_occurrences=int(match.group(2)),
            letter=match.group(3),
            password=match.group(4),
        )
        print(f'{line} is {"valid" if isValid else "invalid"}')
