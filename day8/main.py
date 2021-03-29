PROGRAM = [
    ('nop', 0, False),
    ('acc', 1, False),
    ('jmp', 4, False),
    ('acc', 3, False),
    ('jmp', -3, False),
    ('acc', -99, False),
    ('acc', 1, False),
    ('jmp', -4, False),
    ('acc', 6, False),
]

ACCUMULATOR = 0

if __name__ == '__main__':
    program_counter = 0
    while program_counter < len(PROGRAM):
        (op, arg, executed) = PROGRAM[program_counter]
        if executed:
            break
        PROGRAM[program_counter] = (op, arg, True)
        if op == 'acc':
            ACCUMULATOR += arg
            program_counter = program_counter + 1
            continue
        if op == 'jmp':
            program_counter += arg
            continue
        else:
            program_counter = program_counter + 1

    print(f'Accumulator = {ACCUMULATOR}')
