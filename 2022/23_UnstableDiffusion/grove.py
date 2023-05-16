
# ======================================================================
# Unstable Diffusion
#   Advent of Code 2022 Day 23 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         g r o v e . p y
# ======================================================================
"Grove for the Advent of Code 2022 Day 23 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import namedtuple

# ----------------------------------------------------------------------
#                                                                 tuples
# ----------------------------------------------------------------------
Loc = namedtuple('Loc', 'col, row')

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
ELF = '#'
SPACE = '.'

# ======================================================================
#                                                                  Grove
# ======================================================================


class Grove(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Unstable Diffusion"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.elves = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Loop for every line in the text
        for r_num, row in enumerate(text):

            # 2. Loop for every column in the row:
            for c_num, col in enumerate(row):

                # 3. If there is an elf here, add him/her
                if col == ELF:
                    loc = Loc(col=c_num, row=r_num)
                    self.elves[loc] = Loc(col=0, row=0)

    def rectangle(self):
        "Find the smallest rectangle that contains all the elves"

        # 1. Start with nothing
        min_col = 999999
        max_col = -99999
        min_row = 999999
        max_row = -99999

        # 2. Loop for all the elves
        for elf in self.elves:

            # 3. Adjust the bounding rectangle
            if elf.col < min_col:
                min_col = elf.col
            if elf.col > max_col:
                max_col = elf.col
            if elf.row < min_row:
                min_row = elf.row
            if elf.row > max_row:
                max_row = elf.row

        # 4. Return the minimum and maximum
        return Loc(col=min_col, row=min_row), Loc(col=max_col, row=max_row)

    def is_elf_at(self, loc):
        "Return True if there is an elf at the indicated location"
        return loc in self.elves

    @staticmethod
    def delta(loc, change):
        "Returned the changed locations"
        return Loc(col=loc.col + change.col, row=loc.row + change.row)

    def set_next(self, loc, next_loc):
        "Set the elf's next location"
        self.elves[loc] = Grove.delta(loc, next_loc)

    def is_clear(self, here, locs):
        "Are all the locations empty?"

        # 1. Loop for all of the locations
        for delta in locs:

            # 2. Get the actual location
            there = Grove.delta(here, delta)

            # 3. If there is an elf there, return False
            if self.is_elf_at(there):
                # if len(locs) == 8:
                #     print(f"There is a elf near {here}")
                # else:
                #     print(f"Elf at {here} sees another at {there}")
                return False

        # 4. All clear
        # if len(locs) == 8:
        #     print(f"There is a no elf near {here}")
        # else:
        #     print(f"Elf at {here} see no others at " \
        #           f"{locs[0]}, {locs[1]}, or {locs[2]}")
        return True

    def empty_ground_tiles(self):
        "Returns the empty ground tiles in the smallest rectangle"

        # 1. Determine the bounding rectangle
        min_loc, max_loc = self.rectangle()

        # 2. Compute the size of the rectangle
        width = 1 + max_loc.col - min_loc.col
        height = 1 + max_loc.row - min_loc.row
        size = width * height

        # 3. Return the empty ground tiles
        return size - len(self.elves)

    def __str__(self):
        "Draw the elves in the grove"

        # 1. Quick exit if no elves
        if len(self.elves) == 0:
            return ""

        # 2. Start with nothing
        result = []

        # 3. Get the boundaries
        min_loc, max_loc = self.rectangle()

        # 4. Loop for all the rows
        for r_num in range(min_loc.row, max_loc.row + 1):

            # 5. The row starts with nothing
            row = []

            # 6. Loop for all of the columns in the row
            for c_num in range(min_loc.col, max_loc.col + 1):

                # 7. Add elf or space to the row
                if Loc(col=c_num, row=r_num) in self.elves:
                    row.append(ELF)
                else:
                    row.append(SPACE)

            # 8. Append the row to the result
            result.append(''.join(row))

        # 9. Return the map of the grove
        return '\n'.join(result)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                         g r o v e . p y                        end
# ======================================================================
