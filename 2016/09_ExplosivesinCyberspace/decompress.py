# ======================================================================
# Explosives in Cyberspace
#   Advent of Code 2016 Day 09 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         d e c o m p r e s s . p y
# ======================================================================
"A solver for the Advent of Code 2016 Day 09 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                             Decompress
# ======================================================================


class Decompress(object):   # pylint: disable=R0902, R0205
    "Object for Explosives in Cyberspace"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text

    def expand(self):
        "Expand the text"

        # 1. Handle very short text
        if not self.text or len(self.text) < 1:
            return ''

        # 2. Start with nothing
        start = 0
        result = []
        text = self.text[0].strip()

        # 3. Loop through the text looking for parens
        left = text.find('(', start)
        while left >= 0:

            # 4. Split out the expansion info
            right = text.find(')', left)
            numbers = text[left + 1:right]
            length, repeat = [int(_) for _ in numbers.split('x')]
            # print(text, start, left, right, length, repeat, result)

            # 5. Save the text parts
            if left != start:
                result.append(text[start:left])
            result.append(text[right + 1:right + 1 + length] * repeat)

            # 6. Advence the pointers
            start = right + 1 + length
            left = text.find('(', start)

        # 7. Add the rest of text to the result
        result.append(text[start:])

        # 8. Return the expanded text
        return ''.join(result)

    def expanded(self):
        "Return the size of the expanded text"

        # 1. Handle very short text
        if not self.text or len(self.text) < 1:
            return 0

        # 2. Use the recursive method
        return Decompress.expanded_text(self.text[0].strip())

    @staticmethod
    def expanded_text(text):
        "Return the length of the expanded line"

        # 1. Handle very short text
        if not text or len(text) < 1:
            return 0

        # 2. Start with nothing
        start = 0
        result = 0

        # 3. Loop through the text looking for parens
        left = text.find('(', start)
        while left >= 0:

            # 4. Split out the expansion info
            right = text.find(')', left)
            numbers = text[left + 1:right]
            length, repeat = [int(_) for _ in numbers.split('x')]
            # print(text, 's=', start, 'l=', left, 'r=', right,
            #       'len=', length, 'rep=', repeat, result)

            # 5. Save the text parts
            if left != start:
                result += left - start
            result += repeat * Decompress.expanded_text(text[right + 1: right + 1 + length])

            # 6. Advence the pointers
            start = right + length + 1
            left = text.find('(', start)

        # 7. Add the rest of text to the result
        result += len(text) - start

        # 8. Return the expanded text
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return len(self.expand())

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.expanded()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    d e c o m p r e s s . p y                   end
# ======================================================================
