# ======================================================================
# Rucksack Reorganization
#   Advent of Code 2022 Day 03 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r u c k s a c k . p y
# ======================================================================
"Rucksack for the Advent of Code 2022 Day 03 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
PRIORITY = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# ======================================================================
#                                                               Rucksack
# ======================================================================


class Rucksack(object):   # pylint: disable=R0902, R0205
    "Object for Rucksack Reorganization"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.pockets = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Half goes into each pocket
        size = len(text) // 2
        self.pockets.append(text[:size])
        self.pockets.append(text[size:])

    def both(self):
        "Return characters that appear in both pockets"

        # 1. Start with nothing
        result = []

        # 2. Loop for every character in the first pocket
        for char in self.pockets[0]:

            # 3. If that character is in the second pocket...
            if char in self.pockets[1]:

                # 4. ... Add it to the result if it is a new character
                if char not in result:
                    result.append(char)

        # 5. Return the characters in common
        return ''.join(result)

    @staticmethod
    def priority(chars):
        "Return the priority score"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all the characters
        for char in chars:

            # 3. Get score for this character
            score = 1 + PRIORITY.index(char)

            # 4. Add it to the total
            result += score

        # 5. Return the total score for the characters
        return result

    def badge(self, other, another):
        "Determine the badge letter by comparing rucksacks"

        # 1. Start with nothing
        common = []

        # 2. Loop for the items in my rucksack
        for char in self.text:

            # 3. Is it is both of the other rucksacks?
            if char in other.text and char in another.text:

                # 4. Add it if it is a new character
                if char not in common:
                    common.append(char)

        # 5. Return the items in common
        return ''.join(common)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      r u c k s a c k . p y                     end
# ======================================================================
