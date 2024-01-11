from collections import Counter


TYPES = [
    (5,),          # Five of a kind
    (4, 1),        # Four of a kind
    (3, 2),        # Full house
    (3, 1, 1),     # Three of a kind
    (2, 2, 1),     # Two pair
    (2, 1, 1, 1),  # One pair
]


def score(hand: str):
    #  T -> 10 (A), J -> 11 (B), Q -> 12 (C), K -> 13 (D), A -> 14 (E)
    for old, new in zip('TJQKA', 'abcde'):
        hand = hand.replace(old, new)
    value = int(hand, base=16)
    hand_type = tuple(sorted(Counter(hand).values(), reverse=True))
    for i, t in enumerate(TYPES):
        if hand_type == t:
            return value << 4*(len(TYPES)-i)
    return value


def part1(input: str):
    hands: list[tuple[str, int]] = []
    for line in input.splitlines():
        hand, bid = line.split()
        hands.append((hand, int(bid)))
    hands.sort(key=lambda x: score(x[0]))
    return sum((i+1) * bid for i, (_, bid) in enumerate(hands))


def score_with_joker(hand: str):
    for old, new in zip('TJQKA', 'a1cde'):
        hand = hand.replace(old, new)
    value = int(hand, base=16)

    hand = hand.replace('1', '')
    hand_type = tuple(sorted(Counter(hand).values(),
                      reverse=True)) if hand else (0,)
    hand_type = (hand_type[0] + 5-len(hand), *hand_type[1:])

    for i, t in enumerate(TYPES):
        if hand_type == t:
            return value << 4*(len(TYPES)-i)
    return value


def part2(input: str):
    hands: list[tuple[str, int]] = []
    for line in input.splitlines():
        hand, bid = line.split()
        hands.append((hand, int(bid)))
    hands.sort(key=lambda x: score_with_joker(x[0]))
    return sum((i+1) * bid for i, (_, bid) in enumerate(hands))


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
