# ======================================================================
# Extended Polymerization
#   Advent of Code 2021 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p o l y m e r . p y
# ======================================================================
"A solver for the Advent of Code 2021 Day 14 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import Counter

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                Polymer
# ======================================================================


class Polymer(object):   # pylint: disable=R0902, R0205
    "Object for Extended Polymerization"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.template = ''
        self.rules = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.template = text[0]
            for line in text[1:]:
                pair, add = line.split(' -> ')
                self.rules[pair] = add

    def expand_once(self, pmer):
        "Return the result of a single expansion pass"

        # 1. Start with nothing
        result = []

        # 2. Loop through all of the pairs of letters
        for letter_one, letter_two in zip(pmer, pmer[1:]):
            pair = letter_one + letter_two

            # 3. Is there a rule for this pair, expand it
            if pair in self.rules:
                result.append(letter_one)
                result.append(self.rules[pair])

            # 4. Otherwise just copy the letter
            else:
                result.append(letter_one)

        # 5. The last letter doesn't get expanded
        result.append(pmer[-1])

        # 9. Return the new polymer
        return ''.join(result)

    def expand_template(self, steps, verbose=False):
        "Return the ploymer obtained by expanding the template multiple times"

        # 1. Start with the template (or pair counts from template for part two)
        if self.part2:
            pmer = Counter()
            for letter_one, letter_two in zip(self.template, self.template[1:]):
                pair = letter_one + letter_two
                pmer[pair] += 1
        else:
            pmer = self.template

        # 2. Loop until we expand the polymer the required number of steps
        for _ in range(steps):

            # 3. Use the appropiate expansion routine
            if self.part2:
                pmer = self.expand_two(pmer)
            else:
                pmer = self.expand_once(pmer)
            if verbose:
                print(_, pmer)

        # 3. Return the expanded polymer
        return pmer

    def expand_two(self, pmer):
        "Return the result of a single expansion pass for part2 where counters rule"

        # 1. Start with nothing
        result = Counter()

        # 2. Loop for all of the pairs in the polymer
        for pair in pmer:

            # 3. If there is a rule for it, expand it
            if pair in self.rules:
                letter_one, letter_two = pair
                between = self.rules[pair]
                result[letter_one + between] += pmer[pair]
                result[between + letter_two] += pmer[pair]

            # 4. Else just copy the pair
            else:
                result[pair] += pmer[pair]

        # 5. Return the new polymer (as pair counts)
        return result

    def element_diff(self, pmer):
        "Returns quantity of the most common element minus the least"

        # 1. Part one just counts the letters
        if not self.part2:

            # 2. Count the elements
            knts = Counter(list(pmer))

            # 3. Get the most and least common elements
            most = knts.most_common(1)[0]
            least = knts.most_common()[-1]
            #print(most, least)

            # 4. Return their differences
            return most[1] - least[1]

        # 5. Convert the count of character pairs to character counts (actually count * 2)
        knts = Counter()
        for pair, knt in pmer.items():
            knts[pair[0]] += knt
            knts[pair[1]] += knt

        # 6. Kludge for first and last characters of the template
        knts[self.template[0]] += 1
        knts[self.template[-1]] += 1

        # 7. Get the most and least common elements
        most = knts.most_common(1)[0]
        least = knts.most_common()[-1]
        #print("part2", sum(knts.elements()), most, least, (most[1] - least[1]) // 2)

        # 8. Return their differences
        return (most[1] - least[1]) // 2

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.element_diff((self.expand_template(10, verbose=verbose)))

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.element_diff((self.expand_template(40, verbose=verbose)))


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                       p o l y m e r . p y                      end
# ======================================================================
