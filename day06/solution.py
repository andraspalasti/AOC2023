import math

def possibilities(time: int, record: int):
    assert 0 < time and 0 < record

    # Quadratic formula:
    #   * x1 = (-time + sqrt(time^2 - 4*record)) / -2
    #   * x2 = (-time - sqrt(time^2 - 4*record)) / -2
    # ==> sqrt(time^2 - 4*record) < time
    # ==> x1 < x2

    discriminant = time**2 - 4*record
    assert 0 < discriminant

    left = (-time + math.sqrt(discriminant)) / -2
    right = (-time - math.sqrt(discriminant)) / -2
    return (math.ceil(right-1) - math.floor(left+1) + 1)


def part1(input: str):
    times, records = input.splitlines()

    times = [int(n) for n in times.lstrip('Time:').split()]
    records = [int(n) for n in records.lstrip('Distance:').split()]

    # If hold amount beats record:
    # hold * (time-hold) > record
    # ==> -hold^2 + time*hold - record > 0

    solution = 1
    for time, record in zip(times, records):
        solution *= possibilities(time, record)
    return solution


def part2(input: str):
    time, record = input.splitlines()

    time = int(time.lstrip('Time:').replace(' ', ''))
    record = int(record.lstrip('Distance:').replace(' ', ''))
    return possibilities(time, record)


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

    input = """Time:      7  15   30
Distance:  9  40  200"""
    input = open(Path(__file__).parent / 'input.txt').read()
    if part == 'part1':
        solution = part1(input)
    else:
        solution = part2(input)
    print(f'Solution for {part}: {solution}')
