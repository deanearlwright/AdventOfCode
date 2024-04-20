
# ======================================================================
# Gear Ratios
#   Advent of Code 2023 Day 03 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s c h e m a t i c . p y
# ======================================================================
"Schematic for the Advent of Code 2023 Day 03 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import namedtuple

# ----------------------------------------------------------------------
#                                                                  types
# ----------------------------------------------------------------------
Part = namedtuple('Part', 'col row value symbols stars')

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
PERIOD = '.'
DIGITS = '0123456789'
DELTA = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]
STAR = "*"

# ----------------------------------------------------------------------
#                                                                utility
# ----------------------------------------------------------------------


def surrounding_locs(row, col):
    "Return the (row,col) of the surrounding squares"

    # 1. Start with nothing
    result = set()

    # 2. Loop for all the offsets
    for delta in DELTA:

        # 3. Add that square location
        result.add((row + delta[0], col + delta[1]))

    # 4. Return the surrounding squares
    #print(f"surrounding {row} {col} {result}")
    return result

# ======================================================================
#                                                              Schematic
# ======================================================================


class Schematic(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Gear Ratios"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.symbols = {}
        self.parts = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        assert text is not None and len(text) > 0

        # 1. Loop for all the rows and columns
        for row, line in enumerate(text):
            for col, char in enumerate(line):

                # 2. If it is a symbol, save it
                if char != PERIOD and char not in DIGITS:
                    self.symbols[(row, col)] = char

        # 3. Find and save the numbers
        #print(f"symbols {self.symbols}")
        self.find_numbers()

    def find_numbers(self):

        # 1. Loop for all the rows
        for row, line in enumerate(self.text):

            # 2. Start the row with no number
            start = -1
            surrounding = set()

            # 3. Loop for all the characters in the row
            for col, char in enumerate(line):

                # 4. Have we found a digit? If so, start or add to existing number
                if char in DIGITS:
                    surrounding = surrounding.union(surrounding_locs(row, col))
                    #print(f"found {char} at {row},{col}")
                    if start >= 0:
                        num = num * 10 + int(char)
                    else:
                        num = int(char)
                        start = col

                # 5. If we previously found a number, save it, and reset number search
                elif start >= 0:
                    self.save_number(row, start, num, surrounding)
                    start = -1
                    surrounding = set()

            # 6. If we previously found a number, save it
            if start >= 0:
                self.save_number(row, start, num, surrounding)

    def save_number(self, row, col, num, surrounding):
        "Save a collected number"

        # 1. Start with no symbols found
        symbols = []
        stars = set()

        # 2. Loop for all of the surrounding squares
        for loc in surrounding:

            # 3. If there is a symbol, save it
            if loc in self.symbols:
                symbols.append(self.symbols[loc])

                # 3a. If the symbol is a star save that as well
                if self.symbols[loc] == STAR:
                    stars.add(loc)

        # 4. Create the named tuple
        part = Part(row, col, num, "".join(symbols), stars)

        # 5. Save the part
        #print(f"saving {part} {len(surrounding)}")
        self.parts.append(part)

    def total_parts(self):
        "Return the sum of the numbers adjacent to a symbol"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all the parts
        for part in self.parts:

            # 3. If the part is next to a symbol, add it to the sum
            if len(part.symbols) > 0:
                result += part.value

        # 4. Return the sum of the part numbers
        return result

    def total_gears(self):
        "Return the sum of the part number adjacent to a symbol"

        # 1. Start with nothing
        result = 0
        stars = {}

        # 2. Loop for all the parts
        for part in self.parts:

            # 3. If the part is next to a star, record is next to a symbol, add it to the sum
            for loc in part.stars:
                if loc in stars:
                    stars[loc].append(part)
                else:
                    stars[loc] = [part]

        # 4. Loop for all the collected gear parts
        for parts in stars.values():

            # 5. If there are exactly two parts, accumulate the gear rations
            if len(parts) == 2:
                #print(f"parts {parts}")
                result += parts[0].value * parts[1].value

        # 6. Return the sum of the gear ratios
        return result

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                     s c h e m a t i c . p y                    end
# ======================================================================
