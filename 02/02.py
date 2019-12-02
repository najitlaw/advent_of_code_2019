def run(program, pointer=0, noun=0, verb=0):
    if pointer == 0 and noun and verb:
        program[1] = noun
        program[2] = verb

    opcode = program[pointer]

    if opcode == 99:
        return program

    n1 = program[program[pointer + 1]]
    n2 = program[program[pointer + 2]]

    target = program[pointer + 3]

    if opcode == 1:
        program[target] = n1 + n2
    elif opcode == 2:
        program[target] = n1 * n2
    else:
        return None

    return run(program, pointer + 4)


# read input
data = [int(i) for i in open("input.txt").readline().split(",")]

# result part 1
print(run(data.copy(), noun=12, verb=2)[0])

search = 19690720

for n in range(99):
    for v in range(99):
        result = run(data.copy(), noun=n, verb=v)
        if result and result[0] == search:
            # result part 2
            print(100 * n + v)
