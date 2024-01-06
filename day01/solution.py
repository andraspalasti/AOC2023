def part1(input: str):
    lines = input.splitlines()

    sum = 0
    for line in lines:
        digits = [int(c) for c in line if c.isdigit()]
        assert 0 < len(digits), f"There are no digits in line: '{line}'"
        sum += digits[0]*10 + digits[-1]
    return sum


def part2(input: str):
    lines = input.splitlines()

    vocab = dict(**{str(i): i for i in range(10)}, **{'one': 1, 'two': 2, 'three': 3,
                 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9})

    sum = 0
    for line in lines:
        digits = [digit for i in range(len(line))
                  for digit in vocab.keys() if line[i:].startswith(digit)]
        sum += vocab[digits[0]]*10 + vocab[digits[-1]]
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
