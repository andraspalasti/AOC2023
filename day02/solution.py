def part1(input: str):
    lines = input.splitlines()

    configuration = {'red': 12, 'green': 13, 'blue': 14}

    sum = 0
    for line in lines:
        name, game = line.split(':')
        id = int(name.split()[-1])

        sets = [tuple(pair.strip().split())
                for set in game.split(';') for pair in set.split(',')]
        for count, color in sets:
            if configuration[color] < int(count):
                break
        else:
            sum += id

    return sum


def part2(input: str):
    lines = input.splitlines()

    sum = 0
    for line in lines:
        _, game = line.split(':')

        sets = [tuple(pair.strip().split())
                for set in game.split(';') for pair in set.split(',')]

        cubes = {'red': 0, 'green': 0, 'blue': 0}
        for count, color in sets:
            cubes[color] = max(cubes[color], int(count))
        sum += cubes['red'] * cubes['green'] * cubes['blue']

    return sum


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
