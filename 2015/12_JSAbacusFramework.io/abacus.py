# ======================================================================
# JSAbacusFramework.io
#   Advent of Code 2015 Day 12 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         n u m b e r s . p y
# ======================================================================
"A solver for the Advent of Code 2015 Day 12 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
RE_NUMBER = re.compile("(-?[0-9]+)")
RE_RED = re.compile('":("red")')

# ======================================================================
#                                                                 Abacus
# ======================================================================


class Abacus(object):   # pylint: disable=R0902, R0205
    "Object for JSAbacusFramework.io"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.json = ""

        # 2. Save the text
        if text and len(text) > 0:
            self.json = text[0]

        # 3. For part 2 we elminate the redish part of the json
        if self.part2:
            self.json = Abacus.eliminate_red(self.json)

    def total_json(self):
        "Return the total of numbers in a line (or part of a line of text)"

        # 4. Return the sum of the numbers
        return Abacus.total_line(self.json)

    @staticmethod
    def total_line(line):
        "Return the total of numbers in a line (or part of a line of text)"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the numbers in the line
        for match in RE_NUMBER.finditer(line):

            # 3. Keep a running total
            number = int(match.group(1))
            result += number

        # 4. Return the sum of the numbers
        return result

    @staticmethod
    def eliminate_red(line):
        "Remove the redish stuff from the line"

        # 1. Start at the very beginning
        result = line[:]

        # 2. Start the search
        match = RE_RED.search(result)

        # 3. Loop while we have some read
        while match:

            # 4. Find the left and right braces (there should be some)
            left = Abacus.find_left_brace(result, match.start(1))
            right = Abacus.find_right_brace(result, match.end(1))

            # 5. Add the part before the red object to the result
            result = result[0:left] + result[right + 1:]

            # 6. Do another search to get the ball rolling again
            match = RE_RED.search(result)

        # 7. Return the line without so much red in it
        return result

    @staticmethod
    def find_left_brace(line, pos):
        "Return the location of the left brace (skipping over internal brace pairs)"

        # 1. Start with nothing
        count = 0

        # 2. Loop backwards
        for indx in range(pos, -1, -1):

            # 3. Check for left brace
            if line[indx] == '{':
                if count == 0:
                    return indx
                count -= 1
            # 4. Check for right brace
            elif line[indx] == '}':
                count += 1

        # 5. Should never happen
        print('Unable to find left brace from', pos)
        return 0

    @staticmethod
    def find_right_brace(line, pos):
        "Return the location of the right brace (skipping over internal brace pairs)"

        # 1. Start with nothing
        count = 0

        # 2. Loop forwards
        for indx in range(pos, len(line)):

            # 3. Check for right brace
            if line[indx] == '}':
                if count == 0:
                    return indx
                count -= 1
            # 4. Check for left brace
            elif line[indx] == '{':
                count += 1

        # 5. Should never happen
        print('Unable to find right brace from', pos)
        return len(line)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.total_json()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.total_json()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         a b a c u s . p y                      end
# ======================================================================
