
# ======================================================================
# Warehouse Woes
#   Advent of Code 2024 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         w a r e h o u s e . p y
# ======================================================================
"A solver for the Advent of Code 2024 Day 15 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import box
import robot

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
BOX = "O"
ROBOT = "@"
WALL = "#"
EMPTY = "."

# ======================================================================
#                                                              Warehouse
# ======================================================================


class Warehouse(object):   # pylint: disable=R0902, R0205
    "Object for Warehouse Woes"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.robot = None
        self.boxes = {}
        self.walls = set()
        self.rows = 0
        self.cols = 0

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text()

    def _process_text(self):
        "Assign values from text"

        assert self.text is not None and len(self.text) > 0

        # 1. Loop over the rows of the input text
        for row, line in enumerate(self.text):

            # 2. If this is part of warehouse map
            if line[0] == WALL:
                if row > self.rows:
                    self.rows = row

                # 3. Loop for all of the characters in the line
                for col, char in enumerate(line):
                    loc = (row, col)
                    if self.part2:
                        loc = (row, col + col)
                    if loc[1] > self.cols:
                        self.cols = loc[1]

                    # 4. Process the wall, robot, or box
                    if char == BOX:
                        self.boxes[loc] = box.Box(loc=loc, part2=self.part2)
                        continue
                    if char == ROBOT:
                        self.robot = robot.Robot(loc=loc, part2=self.part2)
                        continue
                    if char == WALL:
                        self.walls.add(loc)
                        if self.part2:
                            self.walls.add((loc[0], loc[1] + 1))

            # 5. Else this robot instructions
            else:
                self.robot.add_instructions(line)

        # 6. Set the walls in place
        self.walls = frozenset(self.walls)
        self.cols += 1
        if self.part2:
            self.cols += 1
        self.rows += 1

    def is_wall(self, loc):
        "Return True if the locations is a wall"
        return loc in self.walls

    def is_box(self, loc):
        "Return the box if there is a box at the location or None if not"
        if loc in self.boxes:
            return self.boxes[loc]
        if self.part2:
            loc2 = (loc[0], loc[1] - 1)
            if loc2 in self.boxes:
                return self.boxes[loc2]
        return None

    def move_box(self, from_loc, to_loc):
        "Move a box"
        # print("move_box", from_loc, to_loc)

        # 0. Precondition axioms
        assert self.is_box(from_loc) is not None
        assert not self.is_wall(to_loc)
        if not self.part2:
            assert self.is_box(to_loc) is None

        # 1. Get the box
        the_box = self.boxes[from_loc]

        # 2. Change the locations of the box
        the_box.move(to_loc)

        # 3. Change the location in the inventory management system
        self.boxes[to_loc] = the_box
        del self.boxes[from_loc]

    def move_robot(self):
        "Move the robot once"
        return self.robot.move(self)

    def move_until_finished(self):
        "Move the robot until it stops"

        more = self.move_robot()
        while more:
            more = self.move_robot()

    def gps(self):
        "Return the combined gps for all of the boxes"
        return sum(box.gps() for box in self.boxes.values())

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part one
        self.move_until_finished()
        return self.gps()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part two
        self.move_until_finished()
        return self.gps()

    def __str__(self):

        # 1. Start empty
        one_row = EMPTY * self.cols
        image = [one_row for _ in range(self.rows)]

        # 2. Add the walls
        for loc in self.walls:
            row = image[loc[0]]
            col = loc[1]
            image[loc[0]] = row[:col] + WALL + row[col + 1:]

        # 3. Add the boxes
        for loc in self.boxes:
            row = image[loc[0]]
            col = loc[1]
            if self.part2:
                image[loc[0]] = row[:col] + "[]" + row[col + 2:]
            else:
                image[loc[0]] = row[:col] + BOX + row[col + 1:]

        # 4. And finally, the robot
        if self.robot is not None:
            loc = self.robot.loc
            row = image[loc[0]]
            col = loc[1]
            image[loc[0]] = row[:col] + ROBOT + row[col + 1:]

        # 5. Return the joined rows
        return "\n".join(image)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                     w a r e h o u s e . p y                    end
# ======================================================================
