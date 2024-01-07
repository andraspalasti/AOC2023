NEAR = [(1, 0), (1, 1), (0, 1), (-1, 1),
        (-1, 0), (-1, -1), (0, -1), (1, -1)]

def is_near_symbol(schematic: list[str], x: int, y: int) -> bool:
    h, w = len(schematic), len(schematic[0])
    for dx, dy in NEAR:
        xx, yy = dx + x, dy + y
        if xx < 0 or w <= xx or yy < 0 or h <= yy:
            continue

        char = schematic[yy][xx]
        if not char.isdigit() and char != '.':
            return True
    return False


def part1(input: str):
    schematic = input.splitlines()
    height, width = len(schematic), len(schematic[0])

    sum = 0
    for y in range(height):
        num = 0
        near_symbol = False
        for x in range(width):
            if schematic[y][x].isdigit():
                num = num*10 + int(schematic[y][x])
                if not near_symbol:
                    near_symbol = is_near_symbol(schematic, x, y)
            elif num != 0:
                if near_symbol:
                    sum += num
                num = 0
                near_symbol = False
        if near_symbol:
            sum += num
    return sum


def part2(input: str):
    schematic = input.splitlines()
    height, width = len(schematic), len(schematic[0])

    gear_to_nums = {}

    for y in range(height):
        num = 0
        gears = set()
        for x in range(width):
            if schematic[y][x].isdigit():
                num = num*10 + int(schematic[y][x])
                for dx, dy in NEAR:
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < width and 0 <= yy < height and schematic[yy][xx] == '*':
                        gears.add((xx, yy))
            elif num != 0:
                for pos in gears:
                    gear_to_nums.setdefault(pos, []).append(num)
                num, gears = 0, set()
        if num != 0:
            for pos in gears:
                gear_to_nums.setdefault(pos, []).append(num)

    sum = 0
    for nums in gear_to_nums.values():
        if len(nums) == 2:
            sum += nums[0] * nums[1]
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

    input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    input = open(Path(__file__).parent / 'input.txt').read()
    if part == 'part1':
        solution = part1(input)
    else:
        solution = part2(input)
    print(f'Solution for {part}: {solution}')
