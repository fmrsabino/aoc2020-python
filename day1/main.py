expenses = [
    1721,
    979,
    366,
    299,
    675,
    1456,
]

targetSum = 2020


def main():
    for i, expense1 in enumerate(expenses):
        for j, expense2 in enumerate(iterable=expenses[i+1:], start=i+1):
            if (j >= len(expenses)):
                break
            if (expense1 + expense2 == targetSum):
                print(f'result = {expense1*expense2}')


if __name__ == '__main__':
    main()
