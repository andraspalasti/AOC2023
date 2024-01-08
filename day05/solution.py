from collections import deque


def convert(map: list[tuple[int, int, int]], n: int):
    for dst, src, length in map:
        if src <= n < src+length:
            return dst + (n - src)
    return n


def part1(input: str):
    parts = input.split('\n\n')

    seeds = [int(seed) for seed in parts[0].split(': ')[-1].split()]

    maps = []
    for part in parts[1:]:
        lines = part.splitlines()
        maps.append([
            tuple(int(n) for n in line.split()) for line in lines[1:]
        ])

    locations = seeds.copy()
    for map in maps:
        for i, n in enumerate(locations):
            locations[i] = convert(map, n)
    return min(locations)


def convert_range(map: list[tuple[int, int, int]], start: int, length: int):
    converted = []
    map = sorted(map, key=lambda x: x[1])
    for dst, low, high in map:
        unchanged = min(low - start, length)
        if unchanged > 0:
            converted.append((start, unchanged))
            start += unchanged
            length -= unchanged
        in_range = min(high - start, length)
        if in_range > 0:
            converted.append((start-low+dst, in_range))
            start += in_range
            length -= in_range
    if length > 0:
        converted.append((start, length))
    return converted


def part2(input: str):
    parts = input.split('\n\n')

    nums = [int(n) for n in parts[0].split(': ')[-1].split()]
    seed_ranges = [(start, length) for start, length in zip(nums[::2], nums[1::2])]

    maps = []
    for part in parts[1:]:
        lines = part.splitlines()

        map = []
        for line in lines[1:]:
            dst, start, length = (int(n) for n in line.split())
            map.append((dst, start, start+length))
        maps.append(map)
        
    unconverted = seed_ranges.copy()
    for map in maps:
        converted = []
        for start, length in unconverted:
            converted.extend(convert_range(map, start, length))
        unconverted = converted
    return min(start for start, _ in unconverted)


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
