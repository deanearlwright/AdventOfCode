# ======================================================================
# Snailfish
#   Advent of Code 2021 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         h o m e w o r k . p y
# ======================================================================
"A solver for the Advent of Code 2021 Day 18 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import number

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                               Homework
# ======================================================================


class Homework(object):   # pylint: disable=R0902, R0205
    "Object for Snailfish"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.pairs = []
        self.sumation = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in text:
                self.pairs.append(number.Number(text=line, part2=part2))

    def sum_them_up(self):
        "Sum the homework numbers"

        # 1. Start with the first one
        result = number.Number(text=str(self.pairs[0]), part2=self.part2)

        # 2. Loop for the rest of the numbers
        for pair in self.pairs[1:]:

            # 3. Add it in
            result.add(pair.pair)

        # 4. Save the sumation
        self.sumation = result

    def largest_magnitude(self):
        "Determine the largest magnitude from adding any two numbers"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the pairs of pairs
        for pair1 in self.pairs:
            for pair2 in self.pairs:
                if pair1 == pair2:
                    continue

                # 2. Add pair2 to pair1 and check the magnitude
                test = number.Number(text=str(pair1))
                test.add(pair2.pair)
                mag = test.magnitude()
                if mag > result:
                    result = mag

                # 3. Add pair1 to pair2 and check the magnitude
                test = number.Number(text=str(pair2))
                test.add(pair1.pair)
                mag = test.magnitude()
                if mag > result:
                    result = mag

        # 4. Return the largest magnitude
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        self.sum_them_up()
        return self.sumation.magnitude()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.largest_magnitude()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      h o m e w o r k . p y                     end
# ======================================================================
