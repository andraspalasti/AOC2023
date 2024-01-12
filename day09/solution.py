def differencies(values: list[int]) -> list[int]:
    if len(values) < 2:
        return []
    return [b-a for a, b in zip(values, values[1:])]


def part1(input: str):
    solution = 0
    for history in input.splitlines():
        history = [int(n) for n in history.split()]

        sequances = [history]
        while any(sequances[-1]):
            sequances.append(differencies(sequances[-1]))
        sequances = list(reversed(sequances))

        for i in range(1, len(sequances)):
            sequances[i].append(sequances[i][-1] + sequances[i-1][-1])

        solution += sequances[-1][-1]
    return solution


def part2(input: str):
    solution = 0
    for history in input.splitlines():
        history = [int(n) for n in history.split()]

        sequances = [history]
        while any(sequances[-1]):
            sequances.append(differencies(sequances[-1]))
        sequances = list(reversed(sequances))

        for i in range(1, len(sequances)):
            sequances[i].insert(0, sequances[i][0] - sequances[i-1][0])

        solution += sequances[-1][0]
    return solution


if __name__ == '__main__':
    import sys
    from pathlib import Path

    part = 'part1'
    if len(sys.argv) > 1:
        part = sys.argv[1]
    if part not in ['part1', 'part2']:
        print(f'Invalid argument provided for part: {part}')
        print(f'Usage: python solution.py [part1, part2]')
        exit(1)

    input = open(Path(__file__).parent / 'input.txt').read()
    if part == 'part1':
        solution = part1(input)
    else:
        solution = part2(input)
    print(f'Solution for {part}: {solution}')
