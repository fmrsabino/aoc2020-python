def read_input() -> []:
    program = []
    for line in open("input.txt"):
        parts = line.split(' ')
        program.append((parts[0], int(parts[1]), False))
    return program


def run_program(program: [str]) -> int:
    accumulator = 0
    program_counter = 0
    while program_counter < len(program):
        (op, arg, executed) = program[program_counter]
        if executed:
            break
        program[program_counter] = (op, arg, True)
        if op == 'jmp':
            program_counter += arg
            continue
        if op == 'acc':
            accumulator += arg
        program_counter = program_counter + 1
    return accumulator


if __name__ == '__main__':
    print(f'Accumulator = {run_program(read_input())}')
