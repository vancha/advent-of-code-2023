input_data = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

with open('input_data.txt','r') as f:
    input_data = f.read()


class platform:
    def __init__(self, input_data):
        split = input_data.strip().split("\n")
        self.grid = [list(i.strip()) for i in split]

    def tilt_left(self):
        work_to_do = True

        while work_to_do:
            work_to_do = False
            for row_idx, row in enumerate(self.grid):
                for idx, spot in enumerate("".join(row)):
                    row = "".join(row)
                    if idx > 0 and spot == "O" and row[idx - 1] == ".":
                        work_to_do = True
                        self.grid[row_idx] = (
                            row[0 : idx - 1] + row[idx] + "." + row[idx + 1 :]
                        )

    def rotate_right(self):
        # i stole this line... it's pretty cool though
        self.grid = list(
            zip(*self.grid[::-1])
        )  # [''.join(list(row)) for row in zip(*self.grid)]

    def tilt_north(self):
        self.rotate_right()  # north faces east
        self.rotate_right()  # north faces south
        self.rotate_right()  # north faces west
        self.tilt_left()  # tilt when north points west
        self.rotate_right()  # make north face up again
   #part two starts here 
    def turn_north_to_left(self):
        self.rotate_right()
        self.rotate_right()
        self.rotate_right()
        #north now points left

    def cycle(self):
        self.tilt_left()#tilt north
        self.rotate_right()
        self.tilt_left()#tilt east
        self.rotate_right()
        self.tilt_left()#tilt south
        self.rotate_right()
        self.tilt_left()#tilt west
        self.rotate_right()
    #part two ends here

    def print(self):
        print()
        for row in self.grid:
            print("".join(row))
        print()

    def get_score(self):
        score = 0
        for row_index, row in enumerate(self.grid):
            for character in "".join(row):
                if character == "O":
                    score += len(self.grid) - row_index
        return score


p = platform(input_data)
p.tilt_north()
score = p.get_score()
print(score)
