def num_in_winning(line: str) -> int:
    winning, my_nums = line.split(':')[1].split('|')
    winning = set(int(n) for n in winning.split())

    in_winning = 0
    for n in my_nums.split():
        n = int(n)
        if n in winning:
            in_winning += 1
    return in_winning

def part1(input: str):
    lines = input.splitlines()
    sum = 0
    for line in lines:
        in_winning = num_in_winning(line)
        if in_winning > 0:
            sum += 2 ** (in_winning-1)
    return sum


def part2(input: str):
    lines = input.splitlines()

    cards = [1] * len(lines)
    for i, line in enumerate(lines):
        in_winning = num_in_winning(line)

        for j in range(in_winning):
            if i+j+1 < len(cards):
                cards[i+j+1] += cards[i]
    return sum(cards)


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

    input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
    input = open(Path(__file__).parent / 'input.txt').read()
    if part == 'part1':
        solution = part1(input)
    else:
        solution = part2(input)
    print(f'Solution for {part}: {solution}')
