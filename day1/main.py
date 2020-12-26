expenses = [
    1721,
    979,
    366,
    299,
    675,
    1456,
]

targetSum = 2020


def solution1(expenses):
    for i, a in enumerate(expenses):
        for b in expenses[i + 1:]:
            if a + b == targetSum:
                return a * b


def solution2(expenses):
    pairs = [(a, b) for i, a in enumerate(expenses) for b in expenses[i + 1:]]
    for (a, b) in pairs:
        if a + b == targetSum:
            return a * b


if __name__ == '__main__':
    result = solution1(expenses)
    print(f'result = {result}')
