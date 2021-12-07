from typing import List

INPUT_PATH = '/Users/tom/advent_of_code/day3_test.txt'

# The gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the
# diagnostic report.
def calculate_gamma_rate(diagnostics: List[str]) -> int:
    # sum the totals for the bits in each position
    totals = [0] * len(diagnostics[0])
    for diagnostic in diagnostics:
        bit_list = [int(x) for x in diagnostic]
        for i in range(0, len(bit_list) - 1):
            totals[i] += bit_list[i]

    # determine the most common bit in each position
    gamma_binary = ''
    for total in totals:
        if total > (len(diagnostics) / 2):
            gamma_binary += '1'
        else:
            gamma_binary += '0'

    print(gamma_binary)
    return int(gamma_binary, 2)


def main():
    file = open(INPUT_PATH)
    puzzle_input = file.read().splitlines()

    print(calculate_gamma_rate(puzzle_input))


if __name__ == '__main__':
    main()
