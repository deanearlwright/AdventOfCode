# ======================================================================
# Like a Rogue
#   Advent of Code 2016 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r o o m . p y
# ======================================================================
"A solver for the Advent of Code 2016 Day 18 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import row

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                   Room
# ======================================================================


class Room(object):   # pylint: disable=R0902, R0205
    "Object for Like a Rogue"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.row = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.row = row.Row(text=text[0], part2=part2)

    def safe(self, rows):
        "Return the number of safe tiles given the number of rows"

        # 1. Start with nothing
        result = 0

        # 2. Handle odd ball cases
        if not self.row or rows < 1:
            return None

        # 3. Start with the initial row
        the_row = row.Row(text=self.row.text)

        # 4. Loop for all of the rows
        for number in range(rows):
            if number > 0 and number % 1000 == 0:
                print(number, result, flush=True)

            # 5. Add it the safe tiles for this row
            result += the_row.count_safe()

            # 6. Advance to the next row
            the_row.tiles = the_row.next_tiles()

        # 7. Return the total number of safe tiles
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.safe(40)

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.safe(400000)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         r o o m . p y                          end
# ======================================================================
