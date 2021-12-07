INPUT_PATH = '/Users/tom/advent_of_code/day2.txt'


class Submarine:
    def __init__(self, hor_pos: int, depth: int, aim: int):
        self.hor_pos = hor_pos  # horizontal position
        self.depth = depth
        self.aim = aim

    # Move according to a given command (commands must 'action X') where `action in ('forward', 'down', 'up')`
    # and x is the number of units to move
    def move(self, command: str):
        action, x = command.split(' ')
        x = int(x)

        if action == 'forward':
            self.hor_pos += x
            self.depth += (self.aim * x)
        elif action == 'down':
            self.aim += x
        elif action == 'up':
            self.aim -= x
        else:
            raise ValueError(f'Invalid command \'{command}\'')


def main():
    file = open(INPUT_PATH)
    puzzle_input = file.read().splitlines()

    sub = Submarine(0, 0, 0)
    for command in puzzle_input:
        sub.move(command)

    print(f'Horizontal position is {sub.hor_pos} and depth is {sub.depth}. '
          f'Multiplied together, this equals {sub.hor_pos * sub.depth}')


if __name__ == '__main__':
    main()
