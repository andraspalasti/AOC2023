import math


def part1(input: str):
    instructions, lines = input.split('\n\n')

    nodes = {}
    for line in lines.splitlines():
        node, neighbors = line.split(' = ')
        nodes[node] = list(neighbors.strip('()').split(', '))

    steps, cur = 0, 'AAA'
    while cur != 'ZZZ':
        dir = instructions[steps % len(instructions)]
        cur = nodes[cur][0 if dir == 'L' else 1]
        steps += 1

    return steps


def part2(input: str):
    instructions, lines = input.split('\n\n')

    nodes: dict[str, list] = {}
    for line in lines.splitlines():
        node, neighbors = line.split(' = ')
        nodes[node] = list(neighbors.strip('()').split(', '))

    starts = [node for node in nodes.keys() if node.endswith('A')]

    circle_lengths = []
    for start in starts:
        step, cur = 0, start

        visited, last_z = {}, 0
        while (r := f'{cur} {step % len(instructions)}') not in visited:
            visited[r] = step
            dir = instructions[step % len(instructions)]
            cur = nodes[cur][0 if dir == 'L' else 1]
            step += 1
            if cur.endswith('Z'): 
                last_z = step

        # We found a circle
        circle_len = step - visited[r]
        assert circle_len == last_z, \
            'The length of the circle must equal the ' \
            'number of steps it takes to reach the end of the path'
        circle_lengths.append(circle_len)
    return math.lcm(*circle_lengths)


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

    input = """LR

11A = (11B, XXX)
22A = (22B, XXX)
11B = (XXX, 11Z)
22B = (22C, 22C)
22C = (22Z, 22Z)
11Z = (11B, XXX)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""
    input = open(Path(__file__).parent / 'input.txt').read()
    if part == 'part1':
        solution = part1(input)
    else:
        solution = part2(input)
    print(f'Solution for {part}: {solution}')
