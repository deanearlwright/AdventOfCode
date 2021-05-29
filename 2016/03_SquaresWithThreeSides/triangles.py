# ======================================================================
# Squares With Three Sides
#   Advent of Code 2016 Day 03 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         t r i a n g l e s . p y
# ======================================================================
"A solver for the Advent of Code 2016 Day 03 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Triangles
# ======================================================================


class Triangles(object):   # pylint: disable=R0902, R0205
    "Object for Squares With Three Sides"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        if text is None:
            self.text = []
        else:
            self.text = text

    def count_triangles(self):
        "Returns the number of triangles in the text"

        # 1. Start with nothing
        result = 0

        # 2. Loop for the rows of text
        for line in self.text:

            # 3. If the line defines a triangle, increment the count
            if Triangles.check_row(line):
                result += 1

        # 4. Return the number of triangles
        return result

    @staticmethod
    def get_numbers(line):
        "Get the numbers from the row as int[]"
        return [int(x) for x in line.replace('  ', ' ').replace('  ', ' ').strip().split(' ')]

    @staticmethod
    def check_row(line):
        "Check an input row to see if it is a trangle"

        # 1. Split out the numbers
        numbers = Triangles.get_numbers(line)

        # 2. Check it is a triangle
        return Triangles.check_sides(numbers)

    @staticmethod
    def check_sides(sides):
        "Return true if the three sides describe a triangle"

        # 1. There must be three (and only three)
        if len(sides) != 3:
            return False

        # 2. Check the sum of the sides
        if sides[0] + sides[1] <= sides[2]:
            return False
        if sides[1] + sides[2] <= sides[0]:
            return False
        if sides[0] + sides[2] <= sides[1]:
            return False

        # 3. I name the triangle
        return True

    def count_col_triangles(self):
        "Count triangles in the columns"

        # 1. Start with nothing
        result = 0
        rows = []

        # 2. Loop for the rows of text
        for line in self.text:

            # 3. Add this line to the rows
            rows.append(Triangles.get_numbers(line))

            # 4. If we have enough number, count the triangles
            if len(rows) == 3:
                if Triangles.check_sides([rows[0][0], rows[1][0], rows[2][0]]):
                    result += 1
                if Triangles.check_sides([rows[0][1], rows[1][1], rows[2][1]]):
                    result += 1
                if Triangles.check_sides([rows[0][2], rows[1][2], rows[2][2]]):
                    result += 1
                rows = []

        # 5. Return the number of triangles
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.count_triangles()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.count_col_triangles()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      t r i a n g l e s . p y                     end
# ======================================================================
