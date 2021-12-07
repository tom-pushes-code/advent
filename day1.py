from typing import List

# Global vars go here
INPUT_PATH = '/Users/tom/advent_of_code/day1.txt'


def count_increases(depths: List[int]) -> int:
    # Given a list of sequential depth measurements,
    # returns a count of the the number of times a depth measurement increases.
    count = 0

    for i in range(0, len(depths)):
        if i == 0:
            continue  # N/A - no previous measurement

        current_measurement = depths[i]
        previous_measurement = depths[i-1]

        if current_measurement > previous_measurement:
            count += 1

    return count


def count_sliding_window_increases(depths: List[int]) -> int:
    # Given a list of sequential depth measurements, slices the measurements into three-value windows (TODO - consider explaining better).
    # Returns a count of the number of times the sum of measurements in this sliding window increases.
    count = 0

    for i in range(0, len(depths) - 3):
        current_window = (depths[i], depths[i+1], depths[i+2])
        next_window = (depths[i+1], depths[i+2], depths[i+3])

        if sum(next_window) > sum(current_window):
            count += 1

    return count


def main():
    # Open file and read input into a list
    file = open(INPUT_PATH)
    puzzle_input = file.read().splitlines()
    puzzle_input = list(map(int, puzzle_input))  # convert strings to ints

    naive_count = count_increases(puzzle_input)
    print(f'Count of depth measurement increases: {naive_count}')

    sliding_window_count = count_sliding_window_increases(puzzle_input)
    print(f'Count of sliding window depth measurement increases: {sliding_window_count}')


if __name__ == '__main__':
    main()
